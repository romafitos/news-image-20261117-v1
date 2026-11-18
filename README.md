# The World in One Day — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/romafitos/news-image-20261117-v1/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/romafitos/news-image-20261117-v1/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One front-page image that sums up the world news of Tuesday 17 November 2026: 33 stories from six continents, laid out as a single broadsheet you can read at a glance. The lead story is the strike on the Kerch Bridge, with a hero illustration of the collapsed span; the rest of the page carries the day's politics, markets, sport, culture and science in short, scannable headlines.

The image is `entry.png` (1024×1024, about 330 KB). `main.py` simply publishes it to the output directory and verifies the copy byte-for-byte.

## Run it

```bash
python3 main.py
```

By default the image is written to `/output/entry.png`. To choose a different folder, set `MAKEFUN_OUTPUT_DIR`:

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

The program refuses to run if the bundled image is missing or larger than 1 MiB, and it prints the output path, size and SHA-256 prefix after a successful verified copy.

<sub>Entered on [make.fun](https://make.fun/?ref=romafitos&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
