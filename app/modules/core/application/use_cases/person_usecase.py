from ..services import person_service
from ..factories import person_factory
from...domain.models.person_model import Person

class PersonUseCase:
    
    def __init__(self):
        self.person_service = person_service.PersonService()
        self.person_factory = person_factory.PersonFactory()
    
    
    def getPersonsUseCase(self):
        data = self.person_service.getPersonsService()
        
        persons: list[Person] = [self.person_factory.toJson(person) for person in data]        
        return persons
    
    
    def getPersonByPkUseCase(self, idPerson: int):
        person = self.person_service.getPersonByPkService(idPerson)
        return person
    
    
    def savePersonsUseCase(self, person: Person):
        
        if not person.firstName or not person.lastName:
            raise Exception("No se ha enviado el nombre correctamente")
        
        if not person.age or not person.phone:
            raise Exception("No se han enviado todos los datos")
        
        
        response = self.person_service.savePersonsService(person)
        return response
    
    
    def updatePersonsUseCase(self, person: Person):
        data = self.person_service.updatePersonsService(person.idPerson, person)
        return data