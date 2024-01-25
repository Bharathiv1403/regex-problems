#Problem 4
"""^ -> Caret it match the begining of the string"""

import re
a="I am Bharathi"
a="this is a python"
match=re.search("^t",a)
print(match)