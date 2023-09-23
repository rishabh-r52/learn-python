import re

str = 'abcd@gmail.com vkkr230@gmail.com @gmail.com'

pattern = r'\S+@\S+[.]com'

regex = re.compile(pattern)

result = regex.findall(str)

print(result)