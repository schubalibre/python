import os
import re

dict = {}

file = open('useradressen.txt', 'r')

for line in file.readlines():
	name = re.search("\w+", line).group()
	nachname = re.search(" (\w+)", line, re.U).group(1)
	zip = re.search(", (\d+)", line).group(1)
	dict[zip] = (nachname, name)

print dict

file.close()

