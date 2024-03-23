# def add(num1,num2):
#     return num1 + num2

# sum = add(5,6)
# print(sum)


# from math import sin,radians

# print(sin(radians(45)))

# x=5
# y=9

# def sumOfTwo(num1, num2):
#     print(num1+num2)

# sumOfTwo(x,y)

# sum = lambda a, b: a + b

# result = sum(x,y)

# print(result)

def fun(a=5, b=6):
    print(a+b)

fun(2,2)
fun(2)
fun()
fun(a=2)
fun(b=2)

def fun2(*num):
    print(type(num))

fun2()

def fun3(**num):
    print(type(num))

fun3()

# redefinition overwrites the old function
def fun():
    print("fun 2")

fun2()
fun(2)