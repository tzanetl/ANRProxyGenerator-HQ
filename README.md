# ANR Proxy Tools

Random collection of Python Scripts for making proxies for Android: Netrunner

## Download Cycle

Downloads high quality card images from a NSG blog post, such as
[this](https://nullsignal.games/blog/the-automata-initiative-is-out-now/). Cards are by default
downloaded to `./cards/`.

Usage:

`python download_cycle.py https://nullsignal.games/blog/the-automata-initiative-is-out-now/`

Show help:

`python download_cycle.py -h`

Requires:

- requests
- beautifulsoup4

## ANR Proxy

Tool to generate printout-ready High Quality images of Android: Netrunner cards for the purpose of proxying.
A forked version of ANRProxyGenerator that uses the image files from /u/LepcisMagna's Netrunner 
scans:

https://redd.it/8pgfbj

Usage:

`python anr_proxy.py`

Show help:

`python anr_proxy.py -h`

Prompts for a directory of jpg and produces a pdf in the same directory.
Print pdf at 100% on letter size page.

If the script fails with "MemoryError", try running it with 64-bit Python.

Requires:

- pillow
