alphabet = "abcdefghijklmnopqrstuvwxyz"
for lettre in alphabet:
    a = lettre
    for lettre in alphabet:
        if a != lettre:
            b = lettre
            c = a + b
            print(c)
