import sys

if len(sys.argv) < 3 : print("Es mussen mindestens 2 Parameter ubergeben werden.")
else :
    i=0
    for x in reversed(sys.argv):
        if i< 2:print x;i=i+1
