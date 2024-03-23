# Strings are Immutable
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a) # String remains the same

a = a + " :D"
print(a)

# rstrip() removes trailing characters
print(a.rstrip("World")) # Remains same
print(a.rstrip(":D")) # Removes ":D"
print(a.rstrip(":D World")) # Removes ":D" but "World" remains

# split() splits the string into a list of strings
str1 = "The Quick Brown Fox Jumps Over The Lazy Dog"
print(str1.split(" "))

# center() places the text in the middle of the console
print()
print(str1.center(50))

# endswith() checks whether or not the string ends with the given substring
print(str1.endswith("og"))
print(str1.endswith("oG"))
print(str1.endswith("Q", 2, 5))

# find() searches for given substring
str2 = "Car is a four wheeler, Bike is a two wheeler"
print(str2.find("wheeler")) # Returns first found's index

# title() and istitle()
str3 = "world health organization"
print(str3)
print(str3.istitle())
print(str3.title())

# isalnum() and isalpha()
str4 = "Vertebrae5"
str5 = "Vertebrae "
print(str1.isalpha())
print(str4.isalnum())
print(str5.isalnum())