d={"OS":("Linux","Open Solaris",["Free BSD","Open BSD"],{"Minix":["V2","V3"]})}
print d["OS"][3]
print d["OS"][2][-1:][0][-2:]
print d.keys()
print d.values()
print d.items()
print "\n"

d={"C": "(2342)", "T": [24, (25, 26)], "P": "dash", 1: {-1: [1, (1,2,3,4)]}}
print d[1]
print d[1][-1]
print d[1][-1][-1:]
print d[1][-1][-1:][-1]
print d[1][-1][-1:][-1][-1:]
print d["C"][-2:]
print d.items()
print "\n"

d={"shell" : ("csh","dash","bsh"), 2 : [3,4,5]}
print d["shell"][:1]
print d[2][2:]
print d.items()
print "\n"

d={"1":3, 1:1, (2,1):("Eins", (5,6), 7, 8, 9), 9:[9,8,7]}
print d[1]
print d[2,1][4:]
print d.values()
print d.items()
print "\n"
