import sys
if len(sys.argv) < 2:
    sys.exit('too few argument')
for arg in sys.argv:
    print("hello i am ", arg)