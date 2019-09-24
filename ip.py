import re
pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{3,3}$")
test = pat.match("10.2.202.10")
print(test)
