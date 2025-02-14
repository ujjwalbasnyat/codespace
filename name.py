import sys
if len(sys.argv) > 2:
    sys.exit('Too many argument')
elif len(sys.argv) < 2:
    sys.exit('too few argument')
print("My name is ", sys.argv[1])