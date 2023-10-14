from flask import jsonify, request, make_response
from ...application.use_cases import user_usecase
from ...application.use_cases import user_usecase
from ...application.factories import user_factory
from ...domain.models.user_model import User
from config.jwt import AuthManager

class UserController:
    
    def __init__(self):
        self.userUseCase = user_usecase.UserUseCase()
        self.userFactory = user_factory.UserFactory()
        self.authManager = AuthManager()
        
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

        
    def getUserByUsername(self):
        
        try:
            user = request.get_json()['username']
            data = self.userUseCase.getUserByUsername(user)
            return jsonify({
                "ok": True,
                "data": self.userFactory.toJson(data) 
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




    def loginUser(self):
        try:
            credentials = request.get_json()
            user = self.authManager.authenticate(credentials)
            if user:
                access_token = self.authManager.create_token(user)
                return jsonify({'ok': True, 'access_token': access_token})
            else:
                return jsonify({"ok": False, "message": "Autenticación fallida"})
                
        except Exception as err:
            return jsonify({
                "ok": False,
                "error": str(err)
            })