class game:
    gamecount = 0

    def __init__ (self,name,type,year):
        self.name = name
        self.type = type
        self.year = year
        game.gamecount += 1

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

    @staticmethod
    def display():
        print("\nUnlike regular methods, static methods do not have access to the instance or class attributes.")
    
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

game1 = game("AC Origins", "RPG", "2016")
game1 = game("Mass Effect Andromeda", "RPG", "2017")

print(f"No. of games = {game.gamecount}")

game.display()
game1.display()