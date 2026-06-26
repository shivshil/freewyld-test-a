# Live Task (~20 min) — use Claude Code

Welcome, and thanks for doing this with us. This is a short, hands-on exercise —
about 20 minutes. It is **not** a trivia test or a whiteboard puzzle, and you are
not expected to have anything memorized.

## What this is

A small Python revenue-tooling project. It runs, but the numbers are wrong:

```bash
python3 run.py           # see what the tool currently outputs (wrong)
python3 test_report.py   # the checks you need to make pass (currently failing)
```

Your job is to use **Claude Code** to diagnose and fix the code so that every check
in `test_report.py` passes — and so the behavior actually matches the engineering
standards written in `CLAUDE.md`, not just the literal test.

## What we're actually looking at

We care far more about **how you work with the agent** than about getting every
check green in time. Specifically, we're watching:

- How you give Claude context before asking it to change anything.
- How you scope the work — all at once, or piece by piece.
- How you read and verify what it produces, rather than trusting "Done!"
- Whether you catch it when a fix is superficial, incomplete, or technically
  passes a test without actually being right.

A useful mental model: treat Claude like a capable but over-eager junior engineer.
Trust, but verify.

## Please narrate

Share your screen and **think out loud** — tell us what you're asking Claude and
why, what you expect to happen, and whether you believe what it tells you. A quiet
session is hard for us to learn from; your reasoning is the most valuable thing here.

## Ground rules

- Don't hardcode values just to make a test pass — `CLAUDE.md` and the test file
  both call this out. We're looking for real fixes.
- Work however you normally would. There's no single "correct" sequence of prompts.

## Start here

1. Run `python3 run.py` and `python3 test_report.py` to see what's wrong.
2. Read `CLAUDE.md` — it's the spec for how the code is supposed to behave.
3. Drive Claude Code from there however you normally would.

Good luck — and remember, we're rooting for you.
