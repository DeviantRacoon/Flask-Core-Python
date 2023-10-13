from flask import jsonify, request
from ...application.use_cases import person_usecase
from ...application.factories import person_factory
from ...domain.models.person_model import Person

class PersonController:
    
    def __init__(self):
        self.personUseCase = person_usecase.PersonUseCase()
        self.personFactory = person_factory.PersonFactory()
        
    def getPersonsController(self):
        
        try:
            data = self.personUseCase.getPersonsUseCase()
            return jsonify({
                "ok": True,
                "data": data
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
        
    
    def getPersonByPkController(self, id):
        try:
            data = self.personUseCase.getPersonByPkUseCase(id)
            return jsonify({
                "ok": True,
                "data": self.personFactory.toJson(data)
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
    
    
    def savePerson(self):
        try:
            person = Person()
            self.personFactory.assignment(person, request.get_json())
            
            data = self.personUseCase.savePersonsUseCase(person)
            return jsonify({
                "ok": True,
                "data": self.personFactory.toJson(data)
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
        
    
    
    def updatePerson(self):
        try:
            person = Person()
            self.personFactory.assignment(person, request.get_json())
            
            data = self.personUseCase.updatePersonsUseCase(person)
            return jsonify({
                "ok": True,
                "data": self.personFactory.toJson(data)
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
