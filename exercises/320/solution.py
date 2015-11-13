import requests
import string
r = requests.get('http://julien.palard.fr/x/words')
text = r.text
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
for k in liste:
    liste[k] = (liste[k]) / tout
for bisou in liste:
    print(bisou + ":", liste[bisou])
