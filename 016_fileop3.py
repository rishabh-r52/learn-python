f1 = open('sample2.txt','w')

f1.write('This file has been modifiied.')

# To append a file, just open in append mode and write the file
# f1.write('Append this')

f1.close()

# File is not automatically 
with open('sample3.txt', 'r+') as file:
    file.write("This line has been added using 'with' keyword.")
    file.seek(0) # Pushes the file pointer back to the start of the file
    content = file.read()
    print(content)

# file.seek(offset, whence)

# 0 (default): Seek from the beginning of the file.
# 1: Seek from the current file position.
# 2: Seek from the end of the file.