def convert(temp):
    new = (9/5)*temp + 32
    return new

try:
    celsius = float(input("Enter temp in celcius: "))
    fahrenheit = convert(celsius)
    print("Temperature in fahrenheit is ", fahrenheit)

except:
    print("Enter numeric value")