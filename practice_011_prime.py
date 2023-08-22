import math

num = int(input("Enter a number: "))
prime = True

for i in range(2, int(num/2) + 1):
    if(num%i == 0):
        prime = False
        break

if (prime):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")