class game:
    def __init__ (self,name,type,year):
        self.name = name
        self.type = type
        self.year = year

    def getName (self):
        return self.name
    
    def getType (self):
        return self.type

    def getYear (self):
        return self.year
    
    def setName (self, name):
        self.name = name
    
    def setType (self, type):
        self.type = type

    def getYear (self, year):
        self.year = year
    
game1 = game("Witcher 3", "RPG", "2015")

print(game1) #Prints the memory location of the game1 object
print(game1.getName())

game1.setName("Kingdom Come Deliverance")

print(game1.name)
print(game1.getName) #Prints the memory location of the getName method
print(game1.getName())

game1.name = "The Division" #We can retrieve / modify the properties of an object without getters / setters
print(game1.name)

print(f"\n- The object game1 -\nName: {game1.name}\nType: {game1.type}\nYear: {game1.year}")
#Formatted String Literals or F-Strings are more efficient and don't require type conversion in expressions