def is_prime(n):
    if n % 2 == 0: return False
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
