import requests
import string
import math
r = open('words')
text = r.read()
alphabet = string.ascii_lowercase
tout = 0
liste = {}
for j in alphabet:
    liste[j] = 0
for i in text:
    for j in alphabet:
        if i == j:
            tout = tout + 1
            liste[j] = int(liste[j]) + 1
for k in alphabet:
    a = (liste[k]) / tout
    liste[k] = a
for bisou in liste:
    print(bisou + ":", liste[bisou])
