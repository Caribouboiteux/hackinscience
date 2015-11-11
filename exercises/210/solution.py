from math_tools import is_prime
a = 0
for i in range(0, 1000):
    if is_prime(i) is True:
        print(i)
        a = a + int(i)
b = int(a)
print(int(b))
