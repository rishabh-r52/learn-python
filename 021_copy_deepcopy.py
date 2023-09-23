import copy

list1 = [1, 2, [3, 4]]
list2 = copy.copy(list1)   # shallow copy
list3 = copy.deepcopy(list1)   # deep copy

list1[0] = 10
list1[2][0] = 30

print(list1)   # [10, 2, [30, 4]]
print(list2)   # [1, 2, [30, 4]]
print(list3)   # [1, 2, [3, 4]]