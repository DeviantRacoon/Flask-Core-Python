from ..services import user_service
from ..factories import user_factory
from...domain.models.user_model import User

class UserUseCase:
    
    def __init__(self):
        self.user_service = user_service.UserService()
        self.user_factory = user_factory.UserFactory()
    
    
    def getUsersUseCase(self):
        data = self.user_service.getUsersService()
        
        Users: list[User] = [self.user_factory.toJson(User) for User in data]        
        return Users
    
    
    def getUserByPkUseCase(self, idUser: int):
        User = self.user_service.getUserByPkService(idUser)
        return self.user_factory.toJson(User)

    
    def saveUsersUseCase(self, user: User):
        
        if not user.username or not user.email or not user.password:
            raise Exception("No se han enviado todos los datos")
        
        if not user.person:
            raise Exception("No has agregado persona al usuario")
        
        response = self.user_service.saveUsersService(user)
        return response
    
    
    def updateUsersUseCase(self, user: User):
        data = self.user_service.updateUsersService(user.idUser, user)
        return self.user_factory.toJson(data)