# ANRProxyGenerator-HQ

Tool to generate printout-ready High Quality images of Android:NetRunner cards for the purpose of proxying.
A forked version of ANRProxyGenerator that uses the image files from /u/LepcisMagna's Netrunner 
scans: \
[https://redd.it/8pgfbj](https://redd.it/8pgfbj)

Usage: \
`anr_proxy.py`

For CLI see: \
`anr_proxy.py -h`

Prompts for a directory of jpg and produces a pdf in the same directory.
Print pdf at 100% on letter size page.

If the script fails with "MemoryError", try running it with 64-bit Python. This should allow it to generate a pdf of the Revised Core Set with 3 copies of each card.

Requires Pillow to run, install with: \
pip install pillow
