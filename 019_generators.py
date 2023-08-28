def gen(x):
    for i in range(x):
        yield i

g1 = gen(5)

print(g1)
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))

#Creates a sequence of values starting from 0 to 4

g2 = gen(500_000_000)

for val in g2:
    print(val)