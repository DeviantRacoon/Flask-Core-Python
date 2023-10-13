from modules.core.domain.models.user_model import User
from .person_factory import PersonFactory
from ..use_cases import person_usecase
from typing import Dict, Union


class UserFactory:

    def __init__(self):
        self.person_factory = PersonFactory()
        self.person_usecase = person_usecase.PersonUseCase()

    def assignment(self, user: User, fields: any) -> None:

        if fields.get('idUser'):
            user.idUser = fields.get('idUser')
        else:
            user.idUser = None

        if fields.get('person'):
            user.person = fields.get('person')
        else:
            user.person = None

        if fields.get('username'):
            user.username = fields.get('username')
        else:
            user.username = None

        if fields.get('email'):
            user.email = fields.get('email')
        else:
            user.email = None

        if fields.get('password'):
            user.password = fields.get('password')
        else:
            user.password = None

        if fields.get('status'):
            user.status = fields.get('status')
        else:
            user.status = None

    def jsonToModel(self, fields: any) -> User:
        user = User()

        if fields.idUser:
            user.idUser = fields.idUser
        else:
            user.idUser = None

        if fields.person:
            user.person = self.person_factory.jsonToModel(fields.person)
        else:
            user.person = None

        if fields.username:
            user.username = fields.username
        else:
            user.username = None

        if fields.email:
            user.email = fields.email
        else:
            user.email = None

        if fields.password:
            user.password = fields.password
        else:
            user.password = None

        if fields.status:
            user.status = fields.status
        else:
            user.status = None

        return user

        
    def toJson(self, user: User) -> Dict[str, Union[str, None]]:
        return {
            "idUser": user.idUser if user.idUser is not None else None,
            "person": self.person_factory.toJson(user.person),
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "status": user.status
        }
        
    def SaveToJson(self, user: User) -> Dict[str, Union[str, None]]:
        return {
            "idUser": user.idUser if user.idUser is not None else None,
            "person": user.person,
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "status": user.status
        }
