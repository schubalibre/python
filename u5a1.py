import re
print re.search('bert','Albert').group()
print re.search('\$','$').group()
print re.search('\$$','asdasdad$').group()
print re.search('^[^^]','D^X').group()
print re.search('[abc]+','xxxaaaddd').group()
print re.search('[abc]','xxxaaaddd').group()
