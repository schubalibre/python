import sys

for i, x in reversed(list(enumerate(sys.argv))):
    if i > 0 : print "%d. %s" % (i,x)
