import sys

digit = sys.argv[1]

for i in range(int(digit)):
    print(' ' * (int(digit) - i - 1), '#' * (i + 1), sep='') 
