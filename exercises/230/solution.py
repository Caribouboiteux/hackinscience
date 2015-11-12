from math_tools import is_prime
import sys
a = 100000002
b = 100000000
while b != a:
    a = a + 1
    b = b + 1
    if is_prime(b) is True:
        print(b)
        sys.exit()
