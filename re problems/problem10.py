#Problem 10
"""{} -> Braces it matches the preceding element from m to n both inclusive -> snytax -> character"""

import re
a="aaabc"
match=re.search("a{2,4}",a)
print(match)
