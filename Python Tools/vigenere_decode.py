#!/bin/python
import sys

def decode(data: str, key: str):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    value = ''
    while len(key) < len(data):
        key = key + key
    kIndex = 0
    vIndex = 0
    for i in data:
        if not i.isalpha():
            value = value + i
            vIndex += 1
        else:
            count = 0
            while alpha[((ord(key[(kIndex)])-65)+count) % 26] != i.upper():
                count += 1
            if data[vIndex].isupper():
                value = value + alpha[count]
            else:
                value = value + alpha[count].lower()
            kIndex += 1
            vIndex += 1
    return value
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        data = input("Enter cipher text: ")
        key = input("Enter the key: ")
        print(f'Decoded Data: {decode(data, key.upper())}')
    else:
        data = sys.argv[1]
        key = sys.argv[2]
        print(f'Decoded Data: {decode(data, key.upper())}')