f1 = open('sample2.txt','w') # If file doesn't exist, Python will create that file.

f1.write("Hello World, This is my Python sample file 2.")

f1.close()

print(f1.read())

# Can't read after file is closed.
# Although execution closed on IO error, the file sample2.txt is created.