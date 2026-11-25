# The Office Joke Open — make.fun entry

[![Make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/dankurniaone/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/rank.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/dankurniaone/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/reward.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

One line of office comedy for the [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) bounty on make.fun.

## The joke

> I set my out-of-office to 'on annual leave' and the calendar auto-invited me to a meeting titled 'While You're Away'.

117 characters, one line. The tool meant to protect your time off invites you to a meeting about your own absence.

## How it runs

`main.py` (Python 3.13, standard library only) writes the joke to `/output/entry.txt` and validates it against the gate: UTF-8 text, 1–200 characters, a single non-blank line.

```sh
python3 main.py --check    # dry run: validate and print the joke
python3 main.py             # write /output/entry.txt
```

## Tournament

Eight candidate lines were drafted and scored 1–5 on specificity, surprise and freshness. The winner scored 4/5/4 = 13, tied with the 47-unread-emails line and winning the tie-break on surprise.
