import re

str = '999-555-1000 999-999-999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

result = phoneNumRegex.findall(str)

print(result)