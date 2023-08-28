file = open('sample.txt','r')

content = file.read()

lines = content.splitlines() # Splits the content into a list of lines separated by newline character

for line in lines:
    print(line)

file.close()

# Same as above. Default mode is 'r'.
file2 = open('sample.txt') 

content_limited = file2.read(60) # Reads only 100 characters

print(content_limited)

file2.close()