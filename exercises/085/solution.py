def sort_a_list(a):
    a.sort(reverse = True)
def sort_by_mark(a):
    a.sort(reverse = True, key = lambda colonne: colonne[0])
    b = str(a)
    c = b.split("],")
    d="]\n".join(c)
    print(d)
def sort_by_name(a):
    a.sort(key = lambda colonne: colonne[1])
    b=str(a)
    c=b.split("],")
    d="]\n".join(c)
    print(d)
