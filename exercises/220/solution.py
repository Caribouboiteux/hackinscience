from math_tools import is_prime
a = []
for i in range(10000, 10050):
    if is_prime(i) is True:
        a.append(str(i))
sortie = ", ".join(a)
print(sortie)
