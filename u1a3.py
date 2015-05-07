import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    if  3 <= len(f) < 6:
        print f
