def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        a = n - 1
        for i in range(1, a):
            s = n % i
            if s == 0:
                return False
            else:
                return True
