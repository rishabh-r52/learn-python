def add(num1,num2):
    return num1 + num2

sum = add(5,6)
print(sum)


from math import sin,radians

print(sin(radians(45)))

x=5
y=9

def sumOfTwo(num1, num2):
    print(num1+num2)

sumOfTwo(x,y)

sum = lambda a, b: a + b

result = sum(x,y)

print(result)