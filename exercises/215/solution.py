from math_tools import is_prime
for i in range(222281, 222381):
    a = bin(i)
    b = a.replace('0', '')
    c = b.replace('b', '')
    if is_prime(len(c)) is True:
        print(i)
