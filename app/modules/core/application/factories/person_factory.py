from modules.core.domain.models.person_model import Person
from typing import Dict, Union

class PersonFactory:
    
    
    def assignment(self, person: Person, fields: any) -> None:
        
        if fields.get('idPerson'):
            person.idPerson = fields.get('idPerson')
        else:
            person.idPerson = None
        
        if fields.get('firstName') :
            person.firstName = fields.get('firstName') 
        else:
            person.firstName = None
        
        if fields.get('secondName') :
            person.secondName = fields.get('secondName') 
        else:
            person.secondName = None
        
        if fields.get('lastName'):
            person.lastName = fields.get('lastName')
        else:
            person.lastName = None
        
        if fields.get('secondLastName'):
            person.secondLastName = fields.get('secondLastName')
        else:
            person.secondLastName = None
        
        if fields.get('phone'):
            person.phone = fields.get('phone')
        else:
            person.phone = None
        
        if fields.get('age'):
            person.age = fields.get('age')
        else:
            person.age = None
    
    
    def jsonToModel(self, fields: any) -> Person:
        person = Person()
        
        if fields.idPerson:
            person.idPerson = fields.idPerson
        else:
            person.idPerson = None
        
        if fields.firstName:
            person.firstName = fields.firstName
        else:
            person.firstName = None
        
        if fields.secondName:
            person.secondName = fields.secondName
        else:
            person.secondName = None
        
        if fields.lastName:
            person.lastName = fields.lastName
        else:
            person.lastName = None
        
        if fields.secondLastName:
            person.secondLastName = fields.secondLastName
        else:
            person.secondLastName = None
        
        if fields.phone:
            person.phone = fields.phone
        else:
            person.phone = None
        
        if fields.age:
            person.age = fields.age
        else:
            person.age = None
    
        return person
    
    
    def toJson(self, person: Person) -> Dict[str, Union[str, None]]:
        return {
            "idPerson": person.idPerson,
            "firstName": person.firstName,
            "secondName": person.secondName,
            "lastName": person.lastName,
            "secondLastName": person.secondLastName,
            "phone": person.phone,
            "age": person.age
        }