from config.database import database as db


class PersonEntity(db.Model):
    __tablename__ = "core_person"
    
    idPerson = db.Column(db.Integer, primary_key = True, autoincrement = True)
    firstName = db.Column(db.String(50))
    secondName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    secondLastName = db.Column(db.String(50))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(15))
    usuarios = db.relationship('UserEntity', backref = 'person', uselist = False, lazy = True)
    
    
    def __init__(self, person):
        
        self.idPerson = person.get('idPerson')
        self.firstName = person.get('firstName')
        self.secondName = person.get('secondName')
        self.lastName = person.get('lastName')
        self.secondLastName = person.get('secondLastName')
        self.phone = person.get('phone')
        self.age = person.get('age')
    
        
    def update(self, person):
        
        self.firstName = person.firstName
        self.secondName = person.secondName
        self.lastName = person.lastName
        self.secondLastName = person.secondLastName
        self.phone = person.phone
        self.age = person.age
          
