#Problem 7
"""? -> Questionmarks it match the preceding element should present zero or one time."""

import re 
a="aab ab abab bbac abc abcbac"
match=re.search("ba?c",a)
print(match)