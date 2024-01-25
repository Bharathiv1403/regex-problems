#Problem 5
"""$ -> Dollar it match the end of the string"""

import re 
a="this is a string"
match=re.search("ing$",a)
print(match)
