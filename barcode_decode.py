#!/bin/python
import cv2
from PIL import Image
from PIL import GifImagePlugin
from pyzbar.pyzbar import decode
import sys

def ReadBarcode(image: str):
	img = cv2.imread(image)
	data = decode(img)
	if not data:
		print(f'Error reading data from {image}')
	else:
		for barcode in data:
			(x, y, w, h) = barcode.rect
			cv2.rectangle(img, (x-10, y-10),
							   (x + w + 10, y + h + 10),
							   (255, 0, 0), 0)
			if barcode.data != "":
				print(f'Barcode Type: {barcode.type}')
				print(f'Found Data: {barcode.data}')
                
def gif2jpg(file_name: str, trans_color: tuple):
    with Image.open(file_name) as im:
        image = im.convert("RGBA")
        datas = image.getdata()
        newData = []
        for item in datas:
            if item[3] == 0:
                newData.append(trans_color)
            else:
                newData.append(tuple(item[:3]))
        image = Image.new("RGB", im.size)
        image.getdata()
        image.putdata(newData)
        new_name = file_name.split('.')[0] + ".jpg"
        image.save('{}'.format(new_name))
        return new_name

if __name__ == '__main__':
    if(len(sys.argv)) != 2:
        fname = input("Path to barcode image: ")
    else:
        fname = sys.argv[1]
    if ".jpg" not in fname:
        fname = gif2jpg(fname, (255, 255, 255))
    ReadBarcode(fname)
