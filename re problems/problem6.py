#Problem 6
"""| -> Or in this we can give two characters if any one of the charater is present in the 
string then it win match that characters."""

import re 
a="this is a string"
match=re.search("a|b",a)
print(match)