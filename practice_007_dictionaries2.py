myDictionary = {}

for i in range(8):
    key = input("Enter a no: ")
    if(not myDictionary.__contains__(key)):
        myDictionary.__setitem__(key,1)
    else:
        myDictionary.__setitem__(key,myDictionary.get(key)+1)

print(myDictionary)