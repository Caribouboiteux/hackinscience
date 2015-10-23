def love_meet(perso1, perso2):
    a = set(perso1) & set(perso2)
    return(a)


def affair_meet(bob, alice, silvester):
    a = set(alice) & set(silvester)
    b = set(a).difference(bob)
    return(b)
