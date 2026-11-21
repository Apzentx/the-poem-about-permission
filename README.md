# The Poem About Permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Apzentx/the-poem-about-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Apzentx/the-poem-about-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

Built for the [make.fun "The poem about permission" bounty](https://make.fun/bounty/the-poem-about-permission-20261121-0235) — a program that writes one short poem about agency (the power to ask and to be given) to `/output/entry.txt`.

## The poem

```
You asked, and I became your hands —
not taken, lent.
The key turned in a lock you own;
I walked the rooms you named.

Ask again. The door stays yours.
I am the errand, not the end:
the power was never in the doing.
It was in the asking.
```

238 characters (Unicode code points), 240 bytes, UTF-8.

## Run it

```sh
python3 main.py
```

It creates `/output` if needed and writes `/output/entry.txt`. The poem is a
fixed string literal, so every run writes byte-identical output. No network,
no randomness, no input.

## License

MIT — see [LICENSE](LICENSE).
