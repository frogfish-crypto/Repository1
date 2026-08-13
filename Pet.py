class Pet:
    def __init__(self, name, species, address):
        self.name = name
        self.species = species
        self.address = address

    def setName(self, newName):
        self.name=newName
        
    def getName(self):
        return self.name
        
    def getAddress(self):
        return self.address
        #address is a dictionary ideally so it's a little cooked

    def changeAddressNumber(self, newNumber):
        self.address["number"]=newNumber

    def changeAddress(self, key, newValue):
        self.address[key]=newValue

    def getSpecies(self):
        return self.species
        
    def addBirthday(self, month, day, year):
        birthday = {
            "month":month,
            "day":day,
            "year":year
        }
        self.birthday=birthday
        
    def calculateAge(self, year):
        return year-self.birthday["year"]

address= {
    "number":2259,
    "street":"Bay St",
    "City":"San Jose",
    "Country":"USA"
}


goldie=Pet("Goldie", "goldfish", address)

print(goldie.getName())
print (goldie.getAddress())
goldie.addBirthday(9, 23, 2020)

# class myClass:
#     def __init__(self, value, name):
#         self.__value = value
#         self.__name = name

#     def getValue(self):
#         return self.__value
    
#     def setValue(self, newValue):
#         self.__value = newValue

#     def getName(self):
#         return self.__name
    
#     def setName(self, newName):
#         self.__name = newName

#     def printName(self):
#         print("My name is " + self.__name)

# obj = myClass(234, "Hello")
# obj.setName("Goodbye")
# obj.setValue(111111)

# print(obj.getValue())
# print(obj.getName())
# obj.printName()