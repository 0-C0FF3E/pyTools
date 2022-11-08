#!/bin/python
import sys

def rotDecode(data: str, num: int):
    if num == 0:
        rounds = 26
    else:
        rounds = 1
    for i in range(rounds):
        for x in range(len(data)):
            if data[x].isalpha():
                if rounds == 26:
                    ltr = chr(ord(data[x])+i)
                else:
                    ltr = chr(ord(data[x])+num)
                if ord(ltr.lower()) > ord('z'):
                    ltr = chr(ord(ltr) - 26)
                elif ord(ltr.upper()) > ord('Z'):
                    ltr = chr(ord(ltr) - 26)
            else:
                ltr = data[x]
            print(f'{ltr}', end='')
        print()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        data = input("Enter string to rotate: ")
        num = int(input("Enter ROT number (0 for all): "))
    else:
        data = sys.argv[1]
        num = int(sys.argv[2])
    rotDecode(data, num)