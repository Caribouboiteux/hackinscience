from itertools import combinations_with_replacement

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for (a,b) in combinations_with_replacement(alphabets, 2):
    if a != b :
        c = a + b 
        print c



