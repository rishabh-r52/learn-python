list1 = [12, 33, "okay", 9.86]
#         0,  1,      2,    3
#        -4, -3,     -2,   -1

print(list1)
print(list1[3])
print(list1[-3])

# [12, 33, 'okay', 9.86]
# 9.86
# 33

# print(list1[-5]) causes error because no element is beyond that

print(list1[0:2])
# [12, 33]

# for score in list1:
#     print(score)

for i in list1:
    print(i)


    marks = [71, 58, 71]

# marks.append(63)
# print(marks)

# print(marks.append(99))
# output: none
# print(marks)

# print(99 in marks)

# print(len(marks))

marks.clear()
print(marks)
# empties the list

lists = [22, 34, 52, 17]
print(lists)
# [22, 34, 52, 17]

lists.insert(2, 70)
print(lists)
# [22, 34, 70, 52, 17]

lists.append(22)
print(lists)
# [22, 34, 70, 52, 17, 22]

lists.remove(22)
print(lists)
# [34, 70, 52, 17, 22]