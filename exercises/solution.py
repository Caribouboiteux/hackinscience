def select_student(liste, note_minimum):
    sortie = {}
    accepte = []
    refuse = []
    for etudiant in liste:
        note = etudiant[1]
        if note < note_minimum:
            refuse.append(etudiant)
        else:
            accepte.append(etudiant)
    accepte = sorted(accepte, reverse=True, key=lambda colonne: colonne[1])
    refuse = sorted(refuse, key=lambda colonne: colonne[1])
    sortie['Refused'] = refuse
    sortie['Accepted'] = accepte
    return sortie
            
