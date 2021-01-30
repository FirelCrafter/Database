with open('Humans', 'r') as h:
    for human in h.readlines():
        hum = human[:-1].split(' ')
        print(hum)

