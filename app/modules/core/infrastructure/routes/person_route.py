from flask import Blueprint, jsonify, make_response
from ..controllers.person_controller import PersonController


personRoute = Blueprint('person', __name__, url_prefix='/person')
personController = PersonController()

@personRoute.route('/')
def getPersons():
    return personController.getPersonsController()


@personRoute.route('/<id>')
def getPersonByPk(id):
    return personController.getPersonByPkController(id)


@personRoute.route('/', methods=['POST'])
def savePerson():
    return personController.savePerson()


@personRoute.route('/', methods=['PUT'])
def updatePerson():
    return personController.updatePerson()
