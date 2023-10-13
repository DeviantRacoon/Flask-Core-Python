from flask import Blueprint
from ..controllers.user_controller import UserController


userRoute = Blueprint('user', __name__, url_prefix='/user')
userController = UserController()

@userRoute.route('/')
def getUsers():
    return userController.getUsersController()


@userRoute.route('/<id>')
def getUserByPk(id):
    return userController.getUserByPkController(id)


@userRoute.route('/', methods=['POST'])
def saveUser():
    return userController.saveUser()


@userRoute.route('/', methods=['PUT'])
def updateUser():
    return userController.updateUser()
