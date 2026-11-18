---
name: interrogate
description: "Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Adversaries try to break a change or design, and only findings proven by a run survive."
---

# Interrogate

Adversaries try to break a change or a design. A finding survives only when a run proves it. Report the findings. Do not apply fixes.

## Frame

The scope is what the user names. Otherwise it is the branch diff from its merge base with the base branch, through the working tree. State the intent with the [in-your-own-words skill](../in-your-own-words/SKILL.md), from the user's message, the commits, and the PR description. Ask the user when the intent is unclear.

## Fan out

Follow [Arena](../arena/SKILL.md) Phase A steps 3 and 4 and Phase B, using the `interrogate reviewers` role from [Native agents](../setup-pstack/references/native-agents.md). Start independent reviewers from the same reviewed HEAD. In each disposable worktree reproduce the scope's staged, unstaged and non-ignored untracked changes, including deletions. Confirm that each reviewer sees the same input as the parent. Reviewers run their checks and keep test artifacts in their own worktrees. Give each reviewer the scope, the intent, and this brief:

> Break this change. Prove each finding with a run against the real code, such as a failing test, a repro script, or command output that shows the wrong behavior. For a design or plan, run a prototype or probe the current tree. Keep repros in your own worktree. Report each finding with a title, the exact command, the output it printed, and the output the intent requires. Leave out anything you did not run. That covers style, naming, structure, and risks that need a future change to matter. No findings is a valid result.

## Verify

Verify each finding per Arena Phase F by inspecting its repro and rerunning the command in the reviewer's worktree or an equivalent disposable copy. Keep a finding when the output shows the failure and the failure breaks the intent. Drop the rest. Merge findings that share a root cause.

Skip arena Phases C, D, and E. Adversaries find different failures, so the verdict keeps every verified finding, not one adversary's list.

## Output

- **Intent**: the restatement.
- **Reviewers**: identify the independent reviewers that completed, their settings and any dropouts. If only the parent could run checks, label that coverage explicitly.
- **Findings**: for each verified finding, the command, its output, how it breaks the intent, and the adversaries that found it. Say “no verified findings” when reviewed evidence yielded none. If no reviewer or parent check ran, report incomplete coverage.
- **Dropped**: for each adversary, the count of dropped findings and why.
