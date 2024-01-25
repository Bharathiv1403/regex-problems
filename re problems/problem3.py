# Problem 3
"""[]-> Square Bracket it contain sequrence of character, using this we can find or search sequene of charater"""

import re
a="I am bharathi ab aczf abc"
match=re.findall("[abc]",a)
print(match)