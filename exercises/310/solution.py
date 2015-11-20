r = open('words')
t = r.read()
a = 0
for i in t:
    if i == "e":
        a = a + 1
print(a)
