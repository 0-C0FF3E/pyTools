#!/bin/python
import sys

alpha = {
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z",
    "/":" ",
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
    "-----":"0"}

def decode(data: str):
    ascii = ""
    for i in data.split(" "):
        ascii = ascii + alpha[i].upper()
    print(f'Decoded Data: {ascii}')
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        data = input("Enter morse text: ")
        decode(data)
    else:
        data = sys.argv[1]
        decode(data)