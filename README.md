# jrstack

## Installation

```sh
codex plugin marketplace add JensenRay/jrstack
codex plugin add jrstack@jrstack
```

## Usage

Try any of these prompts in a new Codex session.

```text
$jrstack:poteto-mode Exporting an empty table drops its column headers. Reproduce it, fix it, and rerun the same export command.
$jrstack:interrogate Review this branch in parallel and show how to reproduce each finding.
$jrstack:setup-pstack Configure the Codex model for each role.
$jrstack:poteto-help Which workflow should I use to pick up an unfinished branch?
```

Parallel workflows use Codex subagents, which inherit the current session’s model by default. Model configuration and session lookup use `uv`. The GitHub PR watcher uses Bun and an authenticated GitHub CLI (`gh`).
