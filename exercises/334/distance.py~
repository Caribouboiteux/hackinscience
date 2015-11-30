from math import sqrt


def euclidean(a, b):
    somme = 0
    dimmension = len(a)
    for i in range(0, dimmension):
        somme = somme + ((b[i] - a[i]) ** 2)
    sortie = somme ** (1 / 2)
    return sortie


def opt_euclidean(a, b):
    somme = 0
    dimmension = len(a)
    for i in range(0, dimmension):
        somme = somme + pow((b[i] - a[i]), 2)
    sortie = sqrt(somme)
    return sortie


def np_euclidean(a, b):
    somme = 0
    dimmension = len(a)
    for i in range(0, dimmension):
        somme = somme + pow((b[i] - a[i]), 2)
    sortie = sqrt(somme)
    return sortie
