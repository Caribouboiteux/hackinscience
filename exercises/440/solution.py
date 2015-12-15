def filtered(items, fonction_conscise):
    sortie = []
    for i in items:
        if fonction_conscise(i) is True:
            sortie.append(str(i))
    return ", ".join(sortie)


if __name__ == '__main__':
    print(filtered(range(0, 101), lambda x: x % 3 == 0))
    print(filtered(range(0, 101), lambda x: x % 5 == 0))
    print(filtered(range(0, 101), lambda x: x % 15 == 0))
