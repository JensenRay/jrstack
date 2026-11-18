---
name: setup-pstack
description: Configure the Codex models, reasoning effort and concurrency used by jrstack workflows. Use for “configure jrstack models”, “pstack budget”, or changes to a role's model.
---

# Setup pstack

Choose how Codex runs jrstack's workers. Save the user's choices in `$CODEX_HOME/jrstack/models.json`, with `~/.codex` as the default Codex home. Each workflow reads this file when it runs.

## Inspect current choices

1. Read [Native agents](references/native-agents.md). Locate the [model settings helper](scripts/models.py) relative to this installed skill. Run `uv run --no-project <absolute-path-to-models.py> show` and `uv run --no-project <absolute-path-to-models.py> roles`. The first command reads the current choices. The second lists the supported role labels. An absent configuration inherits the session's choices for every role.
2. Inspect the native subagent capability in the current session for available models, selectable reasoning efforts, and concurrency. A list of models eligible for the parent chat alone does not establish which models can run a child. When the session cannot enumerate models, offer inheritance and any specific model the user wants to test.
3. Show the existing role choices, including inherited roles. Keep a configured choice unless the user changes it. If the file cannot be read or parsed, report the path and error and resolve that issue before writing.

## Choose and check

Ask which roles to change. Offer the available Codex models and efforts, with `inherit-parent` for either field. On a first run recommend inheritance. For a budget change, offer medium, high, and xhigh effort where the selected model supports them. Let the user select the roles the budget applies to. Ask about a concurrency limit only when the user wants one. An explicit limit is a positive integer. With no limit, the workflows use the session's available slots.

Show the proposed changes. For `arena runners` and `interrogate reviewers`, save an ordered list of model/effort objects when the user chooses individual seats. For `arena cross-judge pool`, list acceptable judges in preference order. A single object applies the same preference to all default seats. A comparison brief can override those choices for one run.

Test each distinct newly requested explicit model/effort pair with one native read-only subagent. Ask it to return a unique marker and wait for its result. Record the requested settings and whether the marker returned. Inheritance uses the current session defaults. If a requested pair fails or the session cannot make a test call, tell the user which choice could not be verified. Keep the file intact and let the user select an available pair or inheritance. Keep a rerun with no requested changes read-only.

## Save

Use the helper's `update` action with a JSON object on standard input, passed as data. Include only the agreed changes. For example, this patch inherits the swarm worker model, explicitly selects high effort and caps concurrent workers at two:

```json
{
  "roles": {
    "swarm workers": { "model": "inherit-parent", "effort": "high" }
  },
  "max_parallel": 2
}
```

Set a role to `null` in the patch to remove its override. A `null` concurrency limit clears the cap. The helper preserves other role assignments and prints the saved configuration. Check its output against the agreed settings, then report the settings path and the verified choices. If the shell reports a write restriction, use the session's normal approval mechanism for the requested write.

## Offer verification skills

Check whether the current project has a `verify-*` skill or an existing harness for driving the real app. If that capability is missing, offer [$jrstack:create-verification-skill](../create-verification-skill/SKILL.md). If the project lacks a model checker, proof, or other formal verifier for a key property, offer [$jrstack:create-formal-verification-skill](../create-formal-verification-skill/SKILL.md). Generate either skill only when the user accepts.
