def draw_n_squares(n):
    a = "+---+"
    b = "---+"
    c = "|   |"
    d = "   |"
    e = a + (int(n) - 1) * b
    f = c + (int(n) - 1) * d
    sortie = (e + "\n" + f + "\n") * n + e
    print(sortie)
