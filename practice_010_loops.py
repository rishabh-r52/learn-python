l1 = ["Harry", "Sohan", "Sachin", "sumit", "Rahul"]

# Classical Approach
for i in l1:
    if (i[0] == 'S' or i[0] == 's'):
        print(f"Greetings, {i}!")

print()

# Python Approach
for i in l1:
    if (i.startswith("S") or i.startswith("s")):
        print(f"Greetings, {i}!")