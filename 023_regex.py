# import re

# str = "i'm here for 2A2 and he's here for 3a3"
# s2 = "hi everyone, i'm Rishabh 23"

# pattern = r'\d\W\d'
# regex = re.compile(pattern)

# result = regex.search(str)
# result2 = regex.findall(str)

# print(result)
# print(result2)

# pat = r'\w\w\w\w\w\w\w'

# rex = re.compile(pat)

# result3 = rex.findall(s2)

# print(result3)


import re

str = "HaHaHaHaHa"

pattern = r'(Ha){3,6}'

regex = re.compile(pattern)

result = regex.search(str)

s2 = result.group()

print(s2)


# import re

# str = 'cat bat rat hat lion pat mat laat'

# pattern = r'.at'

# regex = re.compile(pattern)

# result = regex.findall(str)

# # s2 = result.group()

# print(result)