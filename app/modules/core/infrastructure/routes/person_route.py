from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ..controllers.person_controller import PersonController


personRoute = Blueprint('person', __name__, url_prefix='/person')
personController = PersonController()

@personRoute.route('/')
@jwt_required()
def getPersons():
    return personController.getPersonsController()


@personRoute.route('/<id>')
@jwt_required()
def getPersonByPk(id):
    return personController.getPersonByPkController(id)


@personRoute.route('/', methods=['POST'])
@jwt_required()
def savePerson():
    return personController.savePerson()


@personRoute.route('/', methods=['PUT'])
@jwt_required()
def updatePerson():
    return personController.updatePerson()
