def is_prime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    else:
        for i in range(2, 50):
            print(i)
            s = n % i
            print(s)
            if s == 0:
                return False
        return True
