# Freewyld Live Test

Run these in your terminal (Terminal on Mac, PowerShell on Windows), top to bottom:

```bash
# 1. Install Claude Code (needs Node.js — see note below if this fails)
npm install -g @anthropic-ai/claude-code

# 2. Clone and enter the project
git clone https://github.com/shivshil/freewyld-test-a.git
cd freewyld-test-a

# 3. Start Claude Code
claude
```

Then read `TASK.md` and begin.

> If step 1 says `npm: command not found`, you need Node.js first. **Mac:** `brew install node`. **Windows:** install the LTS from nodejs.org, then reopen PowerShell. Then re-run step 1.

---

## About this project

A small Python revenue-tooling project (standard library only, Python 3). Once you're in:

```bash
python3 run.py           # see what the tool currently outputs
python3 test_report.py   # the checks you need to make pass
```

## Your task

Use **Claude Code** to get `python3 test_report.py` to pass, and to make the code behave according to the standards in `CLAUDE.md`. Work however you normally would with the agent, and please narrate what you're asking it and why. Full brief: see `TASK.md`.
