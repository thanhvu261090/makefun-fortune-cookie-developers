# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/thanhvu261090/makefun-fortune-cookie-developers/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/thanhvu261090/makefun-fortune-cookie-developers/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

A [make.fun](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) entry for **"Fortune Cookie Wisdom for Developers"**: one original fortune-cookie line for a software developer, 120 characters or fewer.

## The entry

> The legacy code you curse today was once someone's proudest deploy — probably yours.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line to `/output/entry.txt`. A built-in gate check enforces the kit's gate before writing: UTF-8 text, 1–120 characters, not only whitespace, and a single line with no leading or trailing whitespace.

```sh
python3 main.py
```

Two runs produce byte-identical output.
