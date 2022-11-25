"""Script designed to print /u/LepcisMagna's Netrunner scans
https://redd.it/8pgfbj

Prompts for directory of image files, produces pdf file
Print pdf at 100% on letter size page.
"""
import argparse
import math
from pathlib import Path
import sys
import tkinter as tk
from tkinter import filedialog

from PIL import Image


RESIZE_HEIGHT = 2100
RESIZE_WIDTH = 1460

# spacing between cards
HORI_SPACING = 0
VERT_SPACING = 0  # best between 0 to 50, otherwise images might fall off the page


def main(image_path=None):
    if not image_path:
        root = tk.Tk()
        root.withdraw()
        image_path = Path(filedialog.askdirectory())
    else:
        image_path = Path(image_path)

    proxy_list = []
    card_image_extensions = ("*.jpg", "*.jpeg", "*.png")
    file_list = []
    for ext in card_image_extensions:
        file_list.extend(image_path.glob(ext))

    for filename in sorted(file_list):
        card_picture = Image.open(filename)
        card_picture = card_picture.resize((RESIZE_WIDTH, RESIZE_HEIGHT))

        # Create a list of all pictures to be printed, uncomment below if printing a pack/box
        proxy_list.append(card_picture)

    proxy_index = 0
    sheet_list = []
    page_count = math.ceil(float(len(proxy_list)) / 9.0)

    for _ in range (0, int(page_count)): # how many pages do we need?
        y_offset = 200
        x_offset = 200
        # a sheet is 3 rows of 3 cards
        sheet = Image.new(
            'RGB',
            ((x_offset+HORI_SPACING)*2+RESIZE_WIDTH*3, (y_offset+VERT_SPACING)*2+RESIZE_HEIGHT*3),
            (255, 255, 255))

        # Fill three rows of three images
        for _ in range(3):
            row = Image.new(
                'RGB',
                ((x_offset+HORI_SPACING)*2+RESIZE_WIDTH*3, RESIZE_HEIGHT),
                (255, 255, 255)
            )
            x_offset = 200
            for j in range (proxy_index, proxy_index+3):
                if j >= len(proxy_list):
                    break
                row.paste(proxy_list[j], (x_offset,0))
                x_offset += RESIZE_WIDTH + HORI_SPACING

            # Combine rows vertically into one image
            sheet.paste(row, (0, y_offset))
            y_offset += RESIZE_HEIGHT + VERT_SPACING
            proxy_index += 3
            if proxy_index >= len(proxy_list):
                break

        sheet_list.append(sheet)
        # sheet.save(f"{image_path.name}_{str(sheet_count)}.png"", 'PNG', quality=100)

    sheet_list[0].save(
        f"{image_path.name}.pdf",
        quality=90,
        resolution=600,
        optimize=True,
        save_all=True,
        append_images=sheet_list[1:]
    )


def cli(argv):
    parser = argparse.ArgumentParser(
        prog="ANR Proxy Generator",
        argument_default=argparse.SUPPRESS
    )
    parser.add_argument("-d", action="store", dest="image_path", help="Image directory")

    parsed_args = parser.parse_args(argv)
    main(**vars(parsed_args))


if __name__ == "__main__":
    cli(sys.argv[1:])
