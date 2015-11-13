import requests
r = requests.get('http://x.mdk.fr/words')
t = r.text
print(t, end="")
