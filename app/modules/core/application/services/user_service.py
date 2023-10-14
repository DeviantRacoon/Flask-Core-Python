from config.database import database
from ...domain.entities.user_entity import UserEntity
from ...domain.entities.person_entity import PersonEntity
from ...domain.models.user_model import User
from ..factories.user_factory import UserFactory
from ..factories.person_factory import PersonFactory


class UserService:
    
    def __init__(self):
        self.db = database
        self.userFactory = UserFactory()
        self.personFactory = PersonFactory()
    
    
    def getUsersService(self):
        users: list[User] = UserEntity.query.all()        
        return users
    
    
    def getUserByUsername(self, username: str):
        user: User = UserEntity.query.filter_by(username = username).first()
        return user
    
    
    def getUserByPkService(self, idUser: int):
        users: User = self.db.get_or_404(UserEntity, idUser)
        return users
    
    
    def saveUsersService(self, user: User):
        try:
            existing_person: PersonEntity = PersonEntity.query.get_or_404(user.person)
        except Exception as err:
            raise Exception(err)
        
        user_json = self.userFactory.SaveToJson(user) 
        new_user = UserEntity(user_json)
        
        self.db.session.add(new_user)
        self.db.session.commit()
    
        return new_user
    
    
    def updateUsersService(self, idUser: int, data: User):
        user = self.db.get_or_404(UserEntity, idUser)
        user.person_id = data.person
        
        user.update(data)
        self.db.session.commit()
        
        return user
