def perfect_shuffle(deck):
    a = []
    b = []
    sortie = []
    for i in range(0, int(len(deck) / 2)):
        c = deck[i]
        a.append(c)
    for i in range(int(len(deck) / 2), int(len(deck))):
        d = deck[i]
        b.append(d)
    for i in range(0, int(len(deck) / 2)):
        sortie.append(a[i])
        sortie.append(b[i])
    return sortie
