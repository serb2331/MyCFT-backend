from classes.user.user import User

class UserList:
    def __init__(self) -> None:
        self.__user_array = []
    
    def get_userlist(self):
        return self.__user_array
    
    def add_user(self, user: User):
        self.__user_array.append(User)