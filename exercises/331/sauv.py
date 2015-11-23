    for mot in range(0, len(mots)):
        if len(mots[mot]) == 5:
            for lettre in mot:
                if lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    coucou = "test"
                else:
                    for k in range(j, len(city)):
                        sortie = sortie.append(city[k])
