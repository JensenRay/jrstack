# Native Codex subagents

## Resolve preferences

Read `${CODEX_HOME:-$HOME/.codex}/jrstack/models.json` before dispatch. The [settings helper](../scripts/models.py) can check the file with `uv run --no-project <absolute-path-to-models.py> show`. The `roles` object maps the role named by the workflow to `{"model": "...", "effort": "..."}`. An absent role, an absent file, or the value `inherit-parent` means leave the corresponding native override unset. Read `max_parallel` as an optional cap on simultaneously active workers. When the settings file is invalid, report its path and the reason and continue with inherited settings where the user's task allows that choice.

`arena runners` and `interrogate reviewers` may instead contain ordered lists. Start one independent seat per entry, including repeated models. For an ordered `arena cross-judge pool`, pick the first available judge with a distinct model if possible. A single settings object supplies the preference for every default seat.

Use the session's native subagent tool when available. With `spawn_agent`, map explicit `model` and `effort` to its `model` and `reasoning_effort` parameters. Follow the current tool's schema and rules for context sharing, overrides and available slots. When an override requires a fresh context, send a complete brief with the goal, evidence, scope, output location and required result. A user-requested comparison can name each seat's settings for that run.

## Run and collect

1. Start independent workers up to the smaller of the configured cap and the session's available capacity. Run queued seats in subsequent waves, releasing completed slots when the tool supports it. Keep handles and wait for terminal results. Record any failure or interruption.
2. Give each writer an isolated worktree or output directory. Native workers can share the parent's filesystem. Name absolute working/output paths in every brief. Give a read-only reviewer instructions to inspect or run checks in the provided scope. Subagents must respect the session's actual permissions.
3. Record each worker's requested settings, returned result and supporting evidence. Tag inherited or unreported model identity accurately. An independent run on an inherited model is still independent work. Multiple runs of an unidentified or identical model do not establish model diversity.
4. If a specific override is unavailable, report it. For ordinary work retry with inherited settings when appropriate, label the replacement, and keep its evidence distinct. In a comparison requiring a named model, record that arm as missing. When delegation is unavailable, run the distinct passes sequentially in the parent and label the evidence as single-agent. Honor an explicit requirement for independent agents by reporting the gap. A plan, request to an agent, or missing result cannot count as a completed run.
