from itertools import combinations_with_replacement
alphabet = "abcdefghijklmnopqrstuvwxyz"
for (a, b) in combinations_with_replacement(alphabet, 2):
    if a != b:
        c = a + b
        print(c)
