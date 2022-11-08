#!/bin/python
import sys
from PIL import Image


def extract(file: str):
    extracted = []
    with Image.open(file) as img:
        w,h = img.size
        out = Image.new('RGB', (w,h), "black")
        byte = []
        for x in range(0,w):
            for y in range(0,h):
                pixel = list(img.getpixel((x,y)))
                r = pixel[0]&1
                g = pixel[1]&1
                b = pixel[2]&1
                out.putpixel((x,y), (r,g,pixel[2]))
    out.show()
    
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        file = input("Name of file: ")
    else:
        file = sys.argv[1]
    extract(file)