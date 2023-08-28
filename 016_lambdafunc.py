def example(fn,x):
    return fn(x)*2

f1 = lambda x : x / 2
f2 = lambda x : x * 2

print(example(f1,10))
print(example(f2,10))