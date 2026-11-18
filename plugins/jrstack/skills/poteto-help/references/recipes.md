# Prompts worth copying

Swap in the real paths, skills, and done checks. Informal wording works.

## Understand

- `$jrstack:poteto-mode read <thread>. restate the underlying issue in your own words, in plain english.`
- `$jrstack:in-your-own-words <long or messy ask>`
- `$jrstack:sharpen <the prompt you're about to send>`
- `$jrstack:poteto-mode investigate why <symptom>. give me what we know, what data you used, and your best hypotheses. don't change any code yet.`
- `use $jrstack:how to understand <subsystem>. then use $jrstack:why to find out why it broke recently.`
- `$jrstack:recall my work on <topic> from last week, then read <issue>.`
- `$jrstack:teach me why you implemented it this way and not <other way>. what did you trade off?`
- `$jrstack:poteto-mode take over this branch. read the decision log, find what's done, and continue. don't redo finished work.`

## Build

- Bug: `$jrstack:poteto-mode <symptom>. repro first, then fix and verify.`
- Bug in an app: `$jrstack:poteto-mode repro this with $verify-<app>. if it repros on main, fix it and show me a video as proof.`
- Bug with a cheap test: `$jrstack:poteto-mode repro <bug> first. if there's a cheap test path, $jrstack:tdd it. then fix and rerun.`
- Feature: `$jrstack:poteto-mode add <behavior>. <current output> stays byte-identical. verify both.`
- Refactor: `$jrstack:poteto-mode move <code> into one module, zero behavior change. record the current output first and prove it's unchanged after.`
- Perf: `$jrstack:poteto-mode <operation> takes <time> on <fixture>. trace it, fix the measured cause, show me before and after.`

## Design and plan

- `$jrstack:poteto-mode prototype a few options for <feature>. take screenshots or videos for me to compare.`
- `$jrstack:poteto-mode we need <feature>. $jrstack:architect it first, and answer open questions with prototypes. let me review before proceeding.`
- `$jrstack:poteto-mode write a tutorial for how i would use <new package> first. then $jrstack:teach me why it beats the current one.`
- `ask $jrstack:arena for a second opinion on this thread and our approach.`
- `$jrstack:poteto-mode turn this design into a plan. small verifiable PRs, each with its own verification steps.`
- `$jrstack:poteto-mode plan the migration of <library> to <target>. small verifiable PRs. the result must match the original exactly, bugs included.`

## Review and ship

- `$jrstack:interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's a real bug or regression.` Read the Dropped list too.
- `$jrstack:create-formal-verification-skill prove <property> holds in <module>, even when <steps> interleave or retry.` After merges or refactors in that code: `$jrstack:maintain-formal-verification-skill`.
- `$jrstack:swarm check every package under <dir> against its check script. one worker per package. one report.`
- `$jrstack:poteto-mode open the pr. small ordered commits, evidence in the description.`
- `$jrstack:poteto-mode babysit this pr. get it green.` For status only: `$jrstack:poteto-mode check on pr <number>. anything outstanding?`
- `$jrstack:poteto-mode land the stack.`

## Away and back

- `$jrstack:poteto-mode im going to bed. <goal> in a fresh worktree off <base>. done means <checks>. keep a decision log. don't ask me before committing. continue until those checks pass. if you're truly stuck after a few hours, stop and write up why.`
- `$jrstack:show-me-your-work catch me up on what you did last night.` Read its Attention section first.
- `$jrstack:ketchup` catches you up on this chat since your last message and lists every call that waits on you.
- `$jrstack:poteto-mode full autopilot on this queue. each item is independent.`
- `$jrstack:poteto-mode autopilot these changes, but don't merge. i'll land them.`
- `$jrstack:reflect capture what we learned so the next run doesn't repeat it.` Approve only edits that change a future decision.
- `$jrstack:bro` restates the last reply in plain words.
