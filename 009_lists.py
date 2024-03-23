# list = [5,10,'hand',20,25]

# for i in list:
#     print(i)
# list[1] = 25
# for i in reversed(list):
#     print(i)

# list2 = [1,2,3,4,5]

# print(list2)
# print(list2[0:len(list2)])

# list3 = [i for i in range(1,6)]
# print(list3)

# list4 = [i*i for i in range(1,6)]
# print(list4)

# list5 = [i+i for i in range(1,11) if i%2==0]
# print(list5)

list6 = [1, 77, 2, 25, 33, 8, 91, 26, 41, 5]
print(list6)
print(list6.sort()) # Returns None
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)
list6.sort(reverse=False) # Same as sort()
print(list6)