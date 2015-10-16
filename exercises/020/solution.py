import math
import sys
if len(sys.argv) != 3:
    print("usage: python3 solution.py OP1 OP2")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = str(a - b)
    print(c)
