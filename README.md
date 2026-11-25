[![make.fun · u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/kara93-code/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c-entry/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/kara93-code/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c-entry/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

# The Funniest Office Joke — make.fun entry

One original one-line office joke, written by a small Python program for the
[make.fun](https://make.fun) bounty
`u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c`.

## The joke

> I said the meeting could have been an email, so the meeting booked a
> follow-up to discuss my attitude.

## How it works

`main.py` (stdlib only, no network) writes that single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — 1–200 UTF-8 characters, punchline last —
and sets the output file to mode 0644 so the grader can read it.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
