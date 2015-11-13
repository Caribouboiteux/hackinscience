import sys
try:
    print(sys.argv[1])
except Exception:
    print("Not enough parameters.")
