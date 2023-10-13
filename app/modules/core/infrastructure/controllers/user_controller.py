from flask import jsonify, request
from ...application.use_cases import user_usecase
from ...application.use_cases import user_usecase
from ...application.factories import user_factory
from ...domain.models.user_model import User

class UserController:
    
    def __init__(self):
        self.userUseCase = user_usecase.UserUseCase()
        self.userFactory = user_factory.UserFactory()
        
    def getUsersController(self):
        
        try:
            data = self.userUseCase.getUsersUseCase()
            return jsonify({
                "ok": True,
                "data": data
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
        
    
    def getUserByPkController(self, id):
        try:
            data = self.userUseCase.getUserByPkUseCase(id)
            return jsonify({
                "ok": True,
                "data": data
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
    
    
    def saveUser(self):
        try:
            user = User()
            self.userFactory.assignment(user, request.get_json())
            
            data = self.userUseCase.saveUsersUseCase(user)
            return jsonify({
                "ok": True,
                "data": self.userFactory.toJson(data)
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
        
    
    
    def updateUser(self):
        try:
            user = User()
            self.userFactory.assignment(user, request.get_json())
            
            data = self.userUseCase.updateUsersUseCase(user)
            return jsonify({
                "ok": True,
                "data": data
            })
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })
