a = int(input("Enter 1 for Yes, 2 for No: "))

match a:
    case 1: print("Yes")
    case 2: print("No")
    case _: print("Bruh")