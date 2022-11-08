#!/bin/python
import sys

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
    
def mod_inv (num, mod):
    for x in range(0,mod + 1):
        if ((num*x)%mod == 1):
            return x
    print("Error resolving mod inverse")
    return None

def decode(data: str):
    for i in range(0,26):
        if (i%2 != 0) and (i != 13):
            for j in range(0,26):
                inv = mod_inv(i,26)
                if inv == None:
                    return None
                eng_test = ''
                for c in data:
                    v = ord(c)
                    if (v >= 65) and (v <= 90):
                        cip = ((v - 65 - j)*inv + 26)%26 + 65
                    elif (v >= 97) and (v <= 122):
                        cip = ((v - 97 - j)*inv + 26)%26 + 97
                    else:
                        cip = v
                    eng_test = eng_test + chr(cip)
                if isEnglish(eng_test):
                    print(f'Decoded Data: {eng_test} [KEY: {i},{j}]')
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        data = input("Enter cipher text: ")
        decode(data)
    else:
        data = sys.argv[1]
        decode(data)