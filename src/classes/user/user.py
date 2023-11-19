class User:
    def __init__(self, id: str, username: str, email: str, fuelType: str, fuelEfficiency: float):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__fuelType=fuelType
        self.__fuelEfficiency=fuelEfficiency
    
    def getId(self):
        return self.__id
    
    def getUsername(self):
        return self.__username
    
    def getEmail(self):
        return self.__email
    
    def getFuelType(self):
        return self.__fuelType
    
    def getFuelEfficiency(self):
        return self.__fuelEfficiency
    
    