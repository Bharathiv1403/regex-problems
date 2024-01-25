#Problem 9
"""+ -> Plus it match the element should present one or more time emty remove"""

import re 
a="aab abbb aab bbac"
match=re.findall("a+",a)
print(match)