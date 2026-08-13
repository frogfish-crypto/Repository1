from Pet import Pet

class Shelter_Pet:

    shelter_address = {
        "number" : 2259,
        "street" : "Bay St.",
        "city" : "San Jose",
        "country" : "USA"
    }

    def __init__ (self, name, species, address, adopted):
        super().__init__(name, species, address)

    def getAdopted(self):
        return self.__adopted
    
    def setAdopt(self, newAdopt):
        self.__adopted = newAdopt

    def addLocation(self, location):
        self.__locationFound = location

    def dateFound(self, month, day, year):
        date={
            "month":month,
            "day":day,
            "year":year
        }
        self.__date=date

    def addBirthday(self):
        super().addBirthday(self.__date)

