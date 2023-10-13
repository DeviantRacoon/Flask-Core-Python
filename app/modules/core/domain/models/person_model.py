class Person:
    
    __idPerson: int 
    __firstName: str 
    __secondName: str
    __lastName: str
    __secondLastName: str
    __phone: str
    __age = int
    
    
    @property
    def idPerson(self):
        return self.__idPerson
    
    @idPerson.setter
    def idPerson(self, value: int):
        self.__idPerson = value
        
    @property
    def firstName(self):
        return self.__firstName
    
    @firstName.setter
    def firstName(self, value: str):
        self.__firstName = value
    
    @property
    def secondName(self):
        return self.__secondName
    
    @secondName.setter
    def secondName(self, value: str):
        self.__secondName = value
    
    @property
    def lastName(self):
        return self.__lastName
    
    @lastName.setter
    def lastName(self, value: str):
        self.__lastName = value
    
    @property
    def secondLastName(self):
        return self.__secondLastName
    
    @secondLastName.setter
    def secondLastName(self, value: str):
        self.__secondLastName = value    
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value: int):
        self.__phone = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value: str):
        self.__age = value
    
    @property
    def fullName(self):
        return f"{self.__firstName or None} {self.__secondName or None} {self.__lastName or None} {self.__secondLastName or None}"
    