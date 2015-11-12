def draw_n_squares(n):
    a = "+---+"
    b = "---+"
    c = "|   |"
    d = "   |"
    e = a + (int(n) - 1) * b
    f = c + (int(n) - 1) * d
    print(str(e))
    u = int(n)
    for i in range(0, u):
        print(str(f))
        print(str(e))
