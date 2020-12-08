


import re
x = "1111221223344444"
y = re.findall(r'((\d)\2+)', x)
print (y)

