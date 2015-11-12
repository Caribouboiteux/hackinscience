def draw_n_squares(n):
    a = "+---+"
    b = "---+"
    c = "|   |"
    d = "   |"
    e = a + (int(n) - 1) * b
    f = c + (int(n) - 1) * d
    print(e)
    u = int(n)
    for i in range(0, u):
        print(f)
        print(e)
