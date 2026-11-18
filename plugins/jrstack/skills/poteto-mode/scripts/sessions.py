"""Print metadata for Codex rollouts started in the given working directory."""

import argparse
import json
import os
import sqlite3
import sys
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path


def indexed_rollouts(home, cwd, session_id):
    """Read only the index columns needed to scope rollouts, including older cwd aliases."""
    indexes = sorted(home.glob("state_*.sqlite"), key=lambda p: p.stat().st_mtime, reverse=True)
    for index in indexes:
        if index.is_symlink():
            continue
        try:
            with closing(sqlite3.connect(index.as_uri() + "?mode=ro", uri=True)) as db:
                query = "SELECT cwd, rollout_path FROM threads"
                args = ()
                if session_id:
                    query += " WHERE id = ?"
                    args = (session_id,)
                known = set()
                matching = set()
                by_cwd = {}
                for recorded, rollout in db.execute(query, args):
                    if not isinstance(rollout, str) or not Path(rollout).is_absolute():
                        continue
                    path = Path(rollout)
                    known.add(path)
                    if isinstance(recorded, str) and Path(recorded).is_absolute():
                        if recorded not in by_cwd:
                            by_cwd[recorded] = Path(recorded).resolve() == cwd
                        if by_cwd[recorded]:
                            matching.add(path)
                return matching, known
        except sqlite3.Error:
            continue
    return set(), set()


def session_record(path, roots, cwd, session_id):
    # A stale index may reference a moved file or a different session. Read the
    # first rollout record only. Message and tool records are never searched.
    try:
        path = path.resolve(strict=True)
        if path.suffix != ".jsonl" or not path.is_file() or not any(path.is_relative_to(r) for r in roots):
            return None
        with path.open("rb") as stream:
            header = json.loads(stream.readline(2 * 1024 * 1024))
        if not isinstance(header, dict) or header.get("type") != "session_meta":
            return None
        meta = header.get("payload")
        if not isinstance(meta, dict):
            return None
        recorded_cwd = meta.get("cwd")
        identifier = meta.get("id") or meta.get("session_id")
        if not isinstance(recorded_cwd, str) or not Path(recorded_cwd).is_absolute():
            return None
        if Path(recorded_cwd).resolve() != cwd or not isinstance(identifier, str) or not identifier:
            return None
        if session_id and identifier != session_id:
            return None
        updated = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
        return dict(path=str(path), cwd=str(cwd), id=identifier, updated_at=updated.isoformat())
    except (OSError, RuntimeError, UnicodeError, ValueError):
        return None


def sessions(home, cwd, session_id=None):
    home = home.expanduser().resolve()
    canonical_cwd = cwd.expanduser().resolve()
    roots = [home / name for name in ("sessions", "archived_sessions")]
    paths, known = indexed_rollouts(home, canonical_cwd, session_id)
    # Older installs and recent rollouts may have no index entry. Only read
    # their session_meta header. Known off-workspace files are never opened.
    for root in roots:
        for path in root.rglob("*.jsonl"):
            if path in known:
                continue
            if not session_id or path.stem.endswith("-" + session_id) or path.stem == session_id:
                paths.add(path)
    records = {}
    for path in paths:
        record = session_record(path, roots, canonical_cwd, session_id)
        if record and (record["id"] not in records or record["updated_at"] > records[record["id"]]["updated_at"]):
            records[record["id"]] = record
    return sorted(records.values(), key=lambda row: (row["updated_at"], row["id"]), reverse=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", type=Path, required=True)
    parser.add_argument("--id", help="exact Codex session ID")
    opts = parser.parse_args()
    try:
        for row in sessions(Path(os.environ.get("CODEX_HOME") or "~/.codex"), opts.cwd, opts.id):
            print(json.dumps(row))
    except OSError as error:
        sys.exit(f"Cannot list Codex session metadata: {error}")
