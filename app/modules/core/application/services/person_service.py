from config.database import database
from ...domain.entities.person_entity import PersonEntity
from ...domain.models.person_model import Person
from ..factories.person_factory import PersonFactory


class PersonService:
    
    def __init__(self):
        self.db = database
        self.personFactory = PersonFactory()
    
    
    def getPersonsService(self):
        persons: list[Person] = PersonEntity.query.all()        
        return persons
    
    
    def getPersonByPkService(self, idPerson: int):
        person: Person = self.db.get_or_404(PersonEntity, idPerson)
        return person
    
    
    def savePersonsService(self, person: Person):
        person_json = self.personFactory.toJson(person)
        new_person = PersonEntity(person_json)

        self.db.session.add(new_person)
        self.db.session.commit()
    
        return new_person
    
    
    def updatePersonsService(self, idPerson: int, data: Person):
        person = self.db.get_or_404(PersonEntity, idPerson)
        
        person.update(data)
        self.db.session.commit()
        
        return person
