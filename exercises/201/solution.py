def is_alpha(chaine):
    lettres = [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]
    for i in chaine:
        if i in lettres:
            return True
        else:
            return False
