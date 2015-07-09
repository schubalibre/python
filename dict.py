dict = {}                          #leeres Dictonary erstellen
for line in open("useradressen.txt"):
        thisline = line.split(",")
#split methode ist fuer jeden String verfuegbar
        name = thisline[0].split(" ")
        plz = thisline[2].split(" ")
        dict[plz[0]] = name[1], name[0]
print dict
