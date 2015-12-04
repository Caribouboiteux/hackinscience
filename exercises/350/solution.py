def encode(n):
    if type(n) == type(b'test'):
        return n
    else:
        b = n.encode('UTF-8')
        return b


def decode(n):
    b = n.decode('UTF-8')
    return b
