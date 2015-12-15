def forward(s, key):
    sortie = []
    for i in s:
        ascii = ord(i)
        if ascii > 64:
            if ascii < 91:
                new_ascii = ascii
                for k in range(0, key):
                    new_ascii = new_ascii + 1
                    if new_ascii > 90:
                        new_ascii = 65
                sortie.append(chr(int(new_ascii)))
            if ascii > 96:
                if ascii < 123:
                    new_ascii = ascii
                    for k in range(0, key):
                        new_ascii = new_ascii + 1
                        ascii = new_ascii
                        if new_ascii > 122:
                            new_ascii = 97
                    sortie.append(chr(int(new_ascii)))
        else:
            sortie.append(i)
    a = "".join(sortie)
    return a


def backward(s, key):
    sortie = []
    for i in s:
        ascii = ord(i)
        if ascii > 64:
            if ascii < 91:
                new_ascii = ascii
                for k in range(0, key):
                    new_ascii = new_ascii - 1
                    if new_ascii < 65:
                        new_ascii = 90
                sortie.append(chr(int(new_ascii)))
            if ascii > 96:
                if ascii < 123:
                    new_ascii = ascii
                    for k in range(0, key):
                        new_ascii = new_ascii - 1
                        ascii = new_ascii
                        if new_ascii < 97:
                            new_ascii = 122
                    sortie.append(chr(int(new_ascii)))
        else:
            sortie.append(i)
    return "".join(sortie)


def caesar_cypher(s, key, method):
    return method(s, key)
