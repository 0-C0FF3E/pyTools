#!/bin/python

c = "22-2-222-55 444-66 6-999 3-2-999-7777 444 9-2-555-55-33-3 60 6-444-555-33-7777 88-7-44-444-555-555 22-666-8-44 9-2-999-7777 8-666 7777-222-44-666-666-555!"

keys = [[' '],
        ['*'],['A','B','C'],['D','E','F'],
        ['G','H','I'],['J','K','L'],['M','N','O'],
        ['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
        
value = []

def numCheck(x: str):
    for z in range(0,len(x)-1):
        if x[z] != x[z+1]:
            return True
    return False
    
def addValue(y: str):
        count = -1
        num = int(y[0])
        special = False
        for z in y:
            if z.isdigit():
                count += 1
            else:
                value.append(keys[num][count])
                special = True
                num = z
        if special == False:
            value.append(keys[num][count])
        else:
            value.append(num)
            
for x in c.split(' '):
    for y in x.split('-'):
        if numCheck(y) == True:
            temp = ''
            flag = False
            for z in y:             
                if z.isalnum():
                    temp = temp + z
                else:
                    addValue(temp)
                    temp = ''
                    value.append(z)
                    flag = True
            if not flag:
                value.append(temp)
        else:
            addValue(y)
    value.append(' ')
            
for i in value:
    print(i, end='')
print()