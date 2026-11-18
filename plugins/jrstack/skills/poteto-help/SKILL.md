---
name: poteto-help
description: "Find the jrstack skill, playbook, or engineering principle for a task and show how to invoke it."
---

# Poteto help

Answer the question, read the workflow you recommend and give one example prompt. If the user asked to do the work, follow [poteto-mode](../poteto-mode/SKILL.md) directly.

## Get started

Start a Codex task with `$jrstack:poteto-mode`, the goal and a check that can pass or fail. The mode selects a playbook and follows its steps. [Prompting](references/prompting.md) and [recipes](references/recipes.md) have examples.

To pick Codex models and reasoning effort for individual roles, run [`$jrstack:setup-pstack`](../setup-pstack/SKILL.md). The default is to inherit the current model. If the project has no way to exercise its real app, use [`$jrstack:create-verification-skill`](../create-verification-skill/SKILL.md).

## Pick a skill

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`$jrstack:poteto-mode`](../poteto-mode/SKILL.md) |
| Check that the agent understood their goal and the problem before it starts | [`$jrstack:in-your-own-words`](../in-your-own-words/SKILL.md) |
| Get a prompt rewritten deeper, not bigger, before sending it: what a top professional would add, their raw material and methods, and an outside check. It returns the prompt and doesn't do the task | [`$jrstack:sharpen`](../sharpen/SKILL.md) |
| Know how code works now, or where new code should live | [`$jrstack:how`](../how/SKILL.md) |
| Know why code is shaped this way, or where a number came from | [`$jrstack:why`](../why/SKILL.md) |
| Understand a change or subsystem, explained plainly | [`$jrstack:teach`](../teach/SKILL.md) |
| Catch up on their own recent work on a topic | [`$jrstack:recall`](../recall/SKILL.md) |
| Catch up on what changed in this chat since their last message, in plain words and small visuals, with every item waiting on them listed and decidable from the reply alone | [`$jrstack:ketchup`](../ketchup/SKILL.md) |
| Catch up like `$jrstack:ketchup`, in a short subtitled video of slides, with the waiting calls as text under it | [`$jrstack:ketchup-video`](../ketchup-video/SKILL.md) |
| Know what a small diff could break outside itself | [`$jrstack:blast-radius`](../blast-radius/SKILL.md) |
| Settle types and module shape before code that crosses a function boundary | [`$jrstack:architect`](../architect/SKILL.md) |
| Get several attempts at one brief, merged into the best one | [`$jrstack:arena`](../arena/SKILL.md) |
| Run parallel checks over slices, or race workers, with Codex workers | [`$jrstack:swarm`](../swarm/SKILL.md) |
| Have independent reviewers examine a diff and try to break it | [`$jrstack:interrogate`](../interrogate/SKILL.md) |
| Fix a bug test-first when a cheap local test exists | [`$jrstack:tdd`](../tdd/SKILL.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`$jrstack:typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| Strip comments before review, using a reviewer that didn't write them | [`$jrstack:no-comments`](../no-comments/SKILL.md) |
| Clean AI tells out of prose | [`$jrstack:unslop`](../unslop/SKILL.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`$jrstack:technical-writing`](../technical-writing/SKILL.md) |
| Hear the last reply again in plain words | [`$jrstack:bro`](../bro/SKILL.md) |
| Give agents a scripted way to drive the app and prove behavior | [`$jrstack:create-verification-skill`](../create-verification-skill/SKILL.md) |
| Bring a verification skill and its feature map back in line with the app | [`$jrstack:maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| Formally verify a race, invariant, or other property that tests rarely reach | [`$jrstack:create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md) |
| Bring a formal verification back in line after the code it covers changed, and learn whether a failure is drift or a bug | [`$jrstack:maintain-formal-verification-skill`](../maintain-formal-verification-skill/SKILL.md) |
| Show a PM or designer what the user sees as a chart checked by a TLA+ model, with the shortest path to each state that breaks a rule | [`$jrstack:statechart`](../statechart/SKILL.md) |
| Vet a performance number before reporting or acting on it | [`$jrstack:benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`$jrstack:figure-it-out`](../figure-it-out/SKILL.md) |
| Keep a decision log during a run, and review it afterward | [`$jrstack:show-me-your-work`](../show-me-your-work/SKILL.md) |
| Pick a model for each role and a reasoning budget | [`$jrstack:setup-pstack`](../setup-pstack/SKILL.md) |
| Turn their own working habits into a personal mode skill | [`$jrstack:automate-me`](../automate-me/SKILL.md) |
| Turn what a finished task taught into skill edits | [`$jrstack:reflect`](../reflect/SKILL.md) |
| Stop agents from repeating the same mistakes in this repo | [`$jrstack:correct`](../correct/SKILL.md) |
| Monitor one open PR until it is ready for review | [`$jrstack:babysit`](../babysit/SKILL.md) |
| Track down a failing PR check | [`$jrstack:fix-ci`](../fix-ci/SKILL.md) |
| Inspect feedback on a PR | [`$jrstack:get-pr-comments`](../get-pr-comments/SKILL.md) |
| Resolve conflicts and validate the result | [`$jrstack:fix-merge-conflicts`](../fix-merge-conflicts/SKILL.md) |
| Clean up code before committing | [`$jrstack:deslop`](../deslop/SKILL.md) |
| Review structure and maintainability | [`$jrstack:thermo-nuclear-code-quality-review`](../thermo-nuclear-code-quality-review/SKILL.md) |
| Prepare a PR for its reviewers | [`$jrstack:make-pr-easy-to-review`](../make-pr-easy-to-review/SKILL.md) |
| Summarize the user's recent commits | [`$jrstack:what-did-i-get-done`](../what-did-i-get-done/SKILL.md) |
| Find their way around jrstack | `$jrstack:poteto-help` |

Close calls:

- `$jrstack:how` explains what the code does. `$jrstack:why` explains the reasons. `$jrstack:teach` runs one or both and explains the result plainly.
- `$jrstack:arena` gives every worker the same brief and merges the best parts. `$jrstack:swarm` splits work into slices or a race and returns one report.
- `$jrstack:interrogate` reviews the diff. `$jrstack:blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `$jrstack:recall` rebuilds context across recent chats. `$jrstack:ketchup` covers only this chat since the user's last message. Resuming one specific chat or branch is the Session pickup playbook.
- `$jrstack:figure-it-out` designs one rigorous run. The Autonomous run playbook drives one task to a finish condition.

## Select a playbook

In `$jrstack:poteto-mode`, describe the outcome. For example:

- "babysit this pr" or "check on pr 123" runs Babysit. It drives the PR to merge-ready and stops there. It doesn't merge unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" runs Autopilot-full. "autopilot, don't merge" runs Autopilot-stack.
- "run the eval playbook" runs Eval.
- "coordinate these independent PRs over several days" runs [Orchestrate](../poteto-mode/playbooks/orchestrate.md).

For work spanning phases, the [Multi-phase plan](../poteto-mode/playbooks/multi-phase-plan.md) writes a plan. For a design question, use the Prototype playbook or `$jrstack:architect`. The [main skill](../poteto-mode/SKILL.md) lists each playbook and the engineering principles it can apply.
