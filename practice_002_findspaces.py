string = "This  string has  more than one spaces  in between   words."
print(string,"\n")

if(string.find("  ") != -1):
    while(string.find("  ") != -1):
        string = string.replace("  ", " ")
    print(string)
else:
    print("Not found")