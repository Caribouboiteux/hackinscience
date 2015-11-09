def is_alpha(chaine):
    for i in chaine:
        if i not in [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]:
            return False
        else:
            return True
