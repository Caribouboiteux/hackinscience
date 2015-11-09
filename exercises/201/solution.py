def is_alpha(chaine):
    lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in chaine:
        if i not in lettres:
            return False
    return True
