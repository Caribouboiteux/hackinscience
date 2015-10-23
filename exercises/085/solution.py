def sort_a_list(a):
    b = sorted(a, reverse=True)
    return(b)


def sort_by_mark(a):
    d = a.sort(reverse=True, key=lambda colonne: colonne[0])
    return(d)


def sort_by_name(a):
    d = a.sort(key=lambda colonne: colonne[1])
    return(d)
