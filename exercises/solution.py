def method():
    if str(method) == "forward":
        method = "forward"
    if str(method) == "backward":
        method = "backward"


def caesar_cypher(s, key, method):
    a = method
    sortie = []
    return type(method)
    if method == "forward":
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
        return "".join(sortie)
    if method == "backward":
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
