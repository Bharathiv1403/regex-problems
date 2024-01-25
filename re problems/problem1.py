#Meta Characters:
    "Meta characters are the Character with special meaning"

# Problem 1
"""(.) -> DOT it matches only single character except the new line(\n)
If the dot changes shape from one eye to the other, the misshapen dot is likely caused by astigmatism
"""

import re
a="I am Bharathi"
match=re.findall(".",a)
print(match)

import re 
a="this is a string"
match=re.findall(".",a)
print(match)
