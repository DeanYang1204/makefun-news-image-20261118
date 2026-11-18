[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/DeanYang1204/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/DeanYang1204/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Built for [make.fun's "Sum up 18 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261118) — $250 in USDC.

# Wednesday 18 November 2026 — the day in one image

Entry for make.fun's **news-image-20261118** bounty ($250, 50 paid places).
One 1024×1024 image that sums up Wednesday 18 November 2026 in four stories,
laid out as a newspaper front page: a header naming the day, a 2×2 grid of
photographic panels, and a short factual caption under each one. All type is
drawn with PIL — no generated panel carries any text, so nothing is garbled.

## The four stories (all happened / first reported on 18 November 2026)

1. **MEASLES RETURNS — US loses measles-free status.**
   More than 5,400 measles cases reported in the US this year, the worst
   outbreak in over three decades (Pan American Health Organization
   declaration).
2. **TRUMP FLIES TO CHINA — Summit in Shenzhen on Nov 19.**
   Trump heads to Shenzhen for the trilateral summit with Xi Jinping and
   Vladimir Putin, meeting on 19 November.
3. **CRIMEA BRIDGE STRUCK — Kerch Strait bridge hit.**
   Ukraine hits the Crimea (Kerch Strait) bridge in a combined
   missile-and-drone operation, as the summit nears; Moscow opens a
   terrorism probe.
4. **FREEZERS DOWN — Cyberattack hits supermarkets in Europe.**
   A cyberattack disables supermarket freezers across seven European
   countries.

No other dated event is shown, and no number beyond the ones above is used.
Yesterday's stories (markets plunge, Hormuz tanker, Kyiv bridges, summit
confirmation) are not presented as today's news — the summit travel story
above is the new development of 18 November.

## How it was made

- Four square panels generated with Kie.ai Grok Imagine Image 2.0
  (text-to-image, 1:1), one per story, photographic/editorial style, with
  no text in the generated images. All four panels were usable on the
  first attempt: a masked nurse vaccinating a child, a presidential jet
  on a dawn runway with red flags, a sea bridge burning at night, and a
  dark supermarket aisle with frosted freezers and a technician.
- The front page was composed from the panels with a Python/Pillow script
  (`~/workspace/makefun-news18-dev/compose.py`, kept out of this repo):
  navy header band with the date, 2×2 grid, captions drawn in DejaVu Sans.
  The first compose had the date clipped and one caption overflowing into
  the next row; both were fixed (smaller date type, shorter measles
  subline, more text room) and the page re-rendered.
- The finished image was read back visually: the date is prominent, all
  four stories are recognisable, captions are legible and match the facts,
  no garbled text, no fifth story.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` beside
it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), checks it is a
JPEG or PNG under 1 MiB, and verifies the copy's sha256 matches the source.
No network access. Two runs write identical bytes.

## Verification

- `entry.png`: JPEG bytes (named `entry.png`, as the rules allow), exactly
  1024×1024, 211,545 bytes (limit 1 MiB), opens as a valid JPEG.
- `main.py` run twice into different output directories: byte-identical
  outputs, sha256 `25b39b36fa3b4582429af0834215a4524dd236adb03721d7a6f1d50ae74050d9`.

## License

MIT — see `LICENSE`.
