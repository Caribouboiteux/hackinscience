import requests
r = requests.get('http://x.mdk.fr/words')
t = r.text
a = 0
for i in t:
    if i == "e":
        a = a + 1
print(a)
