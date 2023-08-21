s = set()

s.add(20)
s.add(20.0)
s.add("20")

print(len(s))
print(s)
# 20 and 20.0 are considered the same and not stored as separate items

s2 = {} #Considered as a dictionary
print(type(s2))

# We can't store a list inside of a set
# s3 = {8,7,12,"Harry",[1,2]}
# print(s3)