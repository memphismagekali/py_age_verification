import random

def yr():
    for x in range(1):
        return random.randint(50,97)

def dy():
    for x in range(1):
        return random.randint(1,30)

def mn():
    for x in range(1):
        return random.randint(1,12)

def av():
    y = yr()
    d = dy()
    m = mn()

    bd = str(m) + '/' + str(d) + '/' + str(y)
    
    r = open('ages.txt', 'r')
    if bd in r.read():
        r.close()
        av()
    else:
        f = open('ages.txt', 'a')
        print '*' + str(bd) + '*'
        f.write(str(bd) + '\n')
        f.close()

av()

