def encode(n):
    if isinstance(n, bytes) is True:
        return n
    else:
        b = n.encode('UTF-8')
        return b


def decode(n):
    b = n.decode('UTF-8')
    return b
