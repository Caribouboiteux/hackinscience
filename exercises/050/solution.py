a = 0
for i in range(1000):
    if int(i) % 3 == 0:
        a = a + i
    if int(i) % 5 == 0:
        a = a + i
    print(int(a))
