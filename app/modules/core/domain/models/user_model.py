from .person_model import Person

class User:
    
    __idUser: int 
    __person: Person 
    __username: str 
    __email: str
    __password: str
    __status = int
    
    
    @property
    def idUser(self):
        return self.__idUser
    
    @idUser.setter
    def idUser(self, value: int):
        self.__idUser = value
    
    @property
    def person(self):
        return self.__person
    
    @person.setter
    def person(self, value: Person):
        self.__person = value
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value: int):
        self.__username = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value: int):
        self.__email = value
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value: int):
        self.__password = value
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value: int):
        self.__status = value
    
    