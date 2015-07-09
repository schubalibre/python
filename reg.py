import re
zeichenk = "-rw-r--r-- 1 root root 1761 2012-02013 22:53 passwd"
mu = ("[wr-]+?", "[toad]+", "o+o", "-+-", "2*2", "2+0*1??")
for item in mu:
    print item, ":", re.search(item, zeichenk).group()


print re.search("bert", "Albert").group()
print re.search("\$","$").group()
print re.search("\$$","$").group()
print re.search("^[^^]","X^X").group()
print re.search("[abc]+","xxxaaddd").group()
print re.search("[abc]", "xxxaaddd").group()
print "\n"

zeichenk = "112-rw-r--r-- 1 root root 1761 2012-02-13 22:53 passwd"
mu = ("1??2","[wr-]+?","[toad]+","o+o","-+-","2*2","2+0*1??")
for item in mu:
	print item, ":", re.search(item, zeichenk).group()
print "\n"

zeichenk = "uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh"
mu = ("uu*?","[0-9]+",".+:.+:+","[ucp]+","[sh]+","(?<=/).+")
for item in mu:
	print item, ":", re.search(item, zeichenk).group()
print "\n"
