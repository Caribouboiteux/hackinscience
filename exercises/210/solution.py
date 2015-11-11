from math_tools import is_prime
a = 0
for i in range(0, 100):
    if is_prime(i) == True:
        a = a + int(i)
print(a)
