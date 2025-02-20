import re
txt = "ababbb bc abc"
x = re.findall("ab*", txt)
print(x)

