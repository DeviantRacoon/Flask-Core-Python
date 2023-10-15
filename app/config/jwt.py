from flask_jwt_extended import JWTManager, create_access_token
from modules.core.application.use_cases.user_usecase import UserUseCase
from modules.core.application.factories.user_factory import UserFactory
from utils.hashing import Hashing
from datetime import timedelta

class AuthManager:
    
    def __init__(self):
        self.userUseCase =  UserUseCase()
        self.userFactory =  UserFactory()
        self.hashing =  Hashing()
    
    def authenticate(self, credentials: dict):
        user = self.userUseCase.getUserByUsername(credentials['username'])
        auth = self.hashing.CheckHash(user.password, credentials['password'])
        
        if auth:
            return user
        else:
            return
             
    
    
    def create_token(self, user):
        access_token = create_access_token(identity = self.userFactory.toJson(user))
        return access_token


def setConfigJWT(app, env):
    app.config['JWT_SECRET_KEY'] = env['TOKEN_PASSWORD']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds = int(env['TIME_TOKEN']))
    
    return JWTManager(app)