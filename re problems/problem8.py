#Problem 8
"""* -> Star it match the element should be present one or more time elements."""

import re 
a="aab abbb aab bbac"
match=re.findall("ab*",a)
print(match)
