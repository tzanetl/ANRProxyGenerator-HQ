# Script designed to print /u/LepcisMagna's Netrunner scans
# https://redd.it/8pgfbj

# Prompts for directory of image files, produces pdf file
# Print pdf at 100% on letter size page.

from PIL import Image
import math
import sys
import glob
import os
import tkinter as tk
from tkinter import filedialog

resize_height = 2100
resize_width = 1460

#spacing between cards
hori_spacing = 0
vert_spacing = 0    #best between 0 to 50, otherwise images might fall off the page


def main(argv):
    if not argv:
        root = tk.Tk()
        root.withdraw()
        image_path = filedialog.askdirectory()
    else:
        image_path = argv[0]

    proxy_list = []
    file_list = sorted(glob.glob(image_path + '/*.jpg'))
    for filename in file_list:
        card_picture = Image.open(filename)
        card_picture = card_picture.resize((resize_width, resize_height))

        # Create a list of all pictures to be printed, uncomment below if printing a pack/box
        proxy_list.append(card_picture)

    proxy_index = 0
    sheet_list = []
    page_count = math.ceil(float(len(proxy_list)) / 9.0)

    for _ in range (0, int(page_count)): #how many pages do we need?
        y_offset = 200
        x_offset = 200
        #a sheet is 3 rows of 3 cards
        sheet = Image.new('RGB', ((x_offset+hori_spacing)*2+resize_width*3, (y_offset+vert_spacing)*2+resize_height*3), (255, 255, 255))
        # Fill three rows of three images
        rows = [Image.new('RGB', ((x_offset+hori_spacing)*2+resize_width*3, resize_height), (255, 255, 255))] * 3
        for row in rows:
            x_offset = 200
            for j in range (proxy_index, proxy_index+3):
                if j >= len(proxy_list):
                    break
                row.paste(proxy_list[j], (x_offset,0))
                x_offset += resize_width + hori_spacing

            # Combine rows vertically into one image
            sheet.paste(row, (0, y_offset))
            y_offset += resize_height + vert_spacing
            proxy_index += 3
            if proxy_index >= len(proxy_list):
                break

        sheet_list.append(sheet)
        #sheet.save(os.path.basename(image_path) + "_" + str(sheet_count)+ '.png', 'PNG', quality=100)

    sheet_list[0].save(os.path.basename(image_path) + '.pdf', quality=90, resolution=600, optimize=True, save_all=True, append_images=sheet_list[1:])

if __name__ == "__main__":
    main(sys.argv[1:])
