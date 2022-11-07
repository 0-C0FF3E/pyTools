#!/bin/python
import sys

def encrypt(plain: str, rails: int, offset: int):
    cipher = ''
    plain = '#'*offset + plain
    length = len(plain)
    fence = [['#']*length for _ in range(rails)]
    rail = 0
    for x in range(length):
        fence[rail][x] = plain[x]
        if rail >= rails-1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr
    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher

def decode(cipher: str, rails: int, offset: int):
    plain = ''
    if offset:
        t = encrypt('o'*offset + 'x'*len(cipher), rails, 0)
        for i in range(len(t)):
            if(t[i] == 'o'):
                cipher = cipher[:i] + '#' + cipher[i:]
    length = len(cipher)
    fence = [['#']*length for _ in range(rails)]
    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    print(f'Decoded Data:{plain}')
    
if __name__ == '__main__':
    if len(sys.argv) != 4:
        data = input("Enter string: ")
        rails = int(input("Number of rails (0 for range): "))
        offset = int(input("Offset value (0 for default): "))
        if(rails == 0):
            rails = int(input("Max rails: "))
            for x in range(2,rails+1):
                decode(data, x, offset)
        else:
            decode(data, rails, offset)
    else:
        data = sys.argv[1]
        rails = int(sys.argv[2])
        offset = int(sys.argv[3])
        decode(data, rails, offset)