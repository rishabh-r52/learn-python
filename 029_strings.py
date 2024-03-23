# String Slicing

names = "Harry,Shubham"
print(names[0:5])

fruit = "Mango"
fruit_len = len(fruit)
print(fruit, "is a", fruit_len, "letter word.")
# Spaces are automatically given between concatenated strings
print(fruit[:3])
print(fruit[3:])
print(fruit[:-2]) # -2 ends at letter 'n'
print(fruit[-2:]) # -2 starts at letter 'n'