def mod(fx):
    def mfx(x,y): # Modified Function
        print("Function is decorated")
        fx(x,y) # Original Function
        print("Function executed")
    return mfx

# Decorator can be used only after its function is defined
@mod
def add(a,b): # Same number of parameters need to be provided for the decorator
    print(a+b)

add(5,10)