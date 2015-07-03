import re
zeichenk = "112-rw-r--r-- 1 root root 1761 2012-02-13 22:53 passwd"
mu = ("1??2","[wr-]+?","[toad]+","o+o","-+-","2*2","2+0*1??")
for item in mu:
	print item, ":", re.search(item, zeichenk).group()
