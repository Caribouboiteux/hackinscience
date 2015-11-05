import math
import sys
if len(sys.argv) != 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if str(sys.argv[2]) == "*":
            c = str(a * b)
            print(c)
        if str(sys.argv[2]) == "+":
            c = str(a + b)
            print(c)
        if str(sys.argv[2]) == "-":
            c = str(a - b)
            print(c)
        if str(sys.argv[2]) == "/":
            c = str(a / b)
            print(c)
        if str(sys.argv[2]) == "%":
            c = str(a % b)
            print(c)
        if str(sys.argv[2]) == "^":
            c = str(a ** b)
            print(c)
        else:
            print("input error")
    except:
        print("input error")
