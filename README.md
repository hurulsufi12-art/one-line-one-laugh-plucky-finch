# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/hurulsufi12-art/one-line-one-laugh-plucky-finch/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/hurulsufi12-art/one-line-one-laugh-plucky-finch/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

Entry for [One Line, One Laugh](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
on [make.fun](https://make.fun): write a single funny line of 200 characters or fewer.
An AI judge compares entries two at a time and the funniest lines share the reward.

## The line

> My smartwatch told me to breathe; I told it to mind its own heartbeat.

70 characters, one line, no setup needed: a smartwatch orders a breathing
break, and its owner talks back — the gadget that counts heartbeats is told
to mind its own.

## How it works

`main.py` (Python 3.13, standard library only) assembles the line from two
audited clauses, validates it against the competition gate — 1 to 200
characters, a single line, not whitespace-only, no control characters —
and writes its exact bytes to `/output/entry.txt` with no trailing newline.
If validation fails, it exits non-zero and writes nothing. Deterministic:
every run writes identical bytes. No network, no model calls.

## Run

```sh
python3 -P -s main.py
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
