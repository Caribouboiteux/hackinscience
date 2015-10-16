a = 0
for i in range(1000):
    if (int(i) % 3 == 0) or (int(i) % 5 == 0):
        a = a + i
b = int(a)
print(a)
