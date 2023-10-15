from config.database import database as db
from .person_entity import PersonEntity


class UserEntity(db.Model):
    __tablename__ = "core_user"

    idUser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(350))
    status = db.Column(db.Integer)
    person_id = db.Column(db.Integer, db.ForeignKey('core_person.idPerson'))

    def __init__(self, person):

        self.idUser = person.get('idUser')
        self.username = person.get('username')
        self.email = person.get('email')
        self.password = person.get('password')
        self.status = person.get('status')
        self.person_id = person.get('person')
        

    def update(self, person):

        self.username = person.username
        self.email = person.email
        self.password = person.password
        self.status = person.status
        self.person_id = person.person
