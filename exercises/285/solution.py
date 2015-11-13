import requests
try:
    r = requests.get('http://mdk.fr/ip')
    t = r.text
    y = t.split("\n")
    print(y[0])
except Exception:
    print("No internet connectivity.")
