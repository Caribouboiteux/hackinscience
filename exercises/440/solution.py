def filtered(items, fonction_conscise):
    even = fonction_conscise
    return even(items)


if __name__ == '__main__':
    print(filtered(range(0, 101), lambda x: x % 3 == 0))
    print(filtered(range(0, 101), lambda x: x % 5 == 0))
    print(filtered(range(0, 101), lambda x: x % 15 == 0))
