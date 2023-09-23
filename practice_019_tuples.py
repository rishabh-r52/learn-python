marksList = [71, 58, 71] # -- this is a list
marksSet = {71, 58, 71} # -- this is a set
marks = (71, 58, 71) # -- this is a tuple
marks2 = 71, 58, 71 # -- this is also a tuple

# print(marksSet)
# {58, 71}

# print(marks)
# (71, 58, 71)

# marks[0] = 99
# editing tuple not possible

# marks += marks
# print(marks)
# (71, 58, 71, 71, 58, 71)

print(marks[0],"appears",marks.count(marks[0]),"times",end="")
# 71 appears 2 times