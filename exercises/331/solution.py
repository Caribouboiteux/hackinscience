import json
a = open('velib.json')
data = json.load(a)
sortie = []
for i in data:
    nom = i["name"].split("- ")
    nom = nom[1]
    i["name"] = nom
for i in data:
    sauvegarde_address = i["address"]
    zip_code = i["address"].split(" ")
    for j in zip_code:
        if len(j) == 5:
            n = 0
            for k in j:
                if k in "0123456789":
                    n = n + 1
                    if n == 5:
                        i["zip_code"] = j
                else:
                    coucou = "test"
    i["address"] = sauvegarde_address
for station in data:
    city = station["address"].split(" ")
    sortie = []
    a = ""
    for j in range(0, len(city)):
        if len(city[j]) == 5:
            n = 0
            for k in city[j]:
                if k in "0123456789":
                    n = n + 1
                    if n == 5:
                        l = j + 1
                        for i in range(l, len(city)):
                            a = a + " " + city[i]
                else:
                    test = 1
    station["city"] = a
for i in data:
    address = i["address"].split(" - ")
    i["address"] = address[0]
obFichier = open('solution.json', "w")
json.dump(data, obFichier)
