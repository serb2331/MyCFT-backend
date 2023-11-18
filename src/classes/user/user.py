class User:
    def __init__(self, id: str, username: str, email: str):
        self.__id = id
        self.__username = username
        self.__email = email
    
    def getId(self):
        return self.__id
    
    def getUsername(self):
        return self.__username
    
    def getEmail(self):
        return self.__email
    
    