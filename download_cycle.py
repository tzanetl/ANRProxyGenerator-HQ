"""Download cycle from the release page

example: https://nullsignal.games/blog/the-automata-initiative-is-out-now/
"""
import argparse
from pathlib import Path
import sys

from bs4 import BeautifulSoup
import requests


class ReleasePage:
    def __init__(self, soup):
        self.soup = soup

    @classmethod
    def from_url(cls, url):
        response = requests.request("GET", url)
        soup = BeautifulSoup(response.content, "html.parser")
        return cls(soup)

    def iter_cards(self):
        for element in self.soup.find_all("img", attrs={"data-id": True, "data-full-url": True}):
            yield int(element.attrs["data-id"]), element.attrs["data-full-url"]


def main(url, output):
    output = Path(output)
    rp = ReleasePage.from_url(url)
    for data_id, card_url in rp.iter_cards():
        file_ext = card_url.rsplit(".", maxsplit=1)[1]
        file_name = f"{data_id}.{file_ext}"
        with open(output.joinpath(file_name), mode="wb") as fs:
            for chunk in requests.request("GET", card_url, stream=True).iter_content(1024):
                fs.write(chunk)


def cli(argv):
    parser = argparse.ArgumentParser(
        prog="ANR Cycle Downloader",
        argument_default=argparse.SUPPRESS
    )
    parser.add_argument("url", action="store", help="Release post url")
    parser.add_argument(
        "-o", action="store", dest="output", help="Download output folder", type=str,
        default="./cards"
    )

    parsed_args = parser.parse_args(argv)
    main(**vars(parsed_args))

if __name__ == "__main__":
    cli(sys.argv[1:])
