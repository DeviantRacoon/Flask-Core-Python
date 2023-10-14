from flask import Blueprint
from flask_jwt_extended import jwt_required
from ..controllers.user_controller import UserController


userRoute = Blueprint('user', __name__, url_prefix='/user')
userController = UserController()

@userRoute.route('/')
@jwt_required()
def getUsers():
    return userController.getUsersController()


@userRoute.route('/username', methods=['POST'])
@jwt_required()
def getUserByUsername():
    return userController.getUserByUsername()


@userRoute.route('/<id>')
@jwt_required()
def getUserByPk(id):
    return userController.getUserByPkController(id)


@userRoute.route('/', methods=['POST'])
@jwt_required()
def saveUser():
    return userController.saveUser()


@userRoute.route('/', methods=['PUT'])
@jwt_required()
def updateUser():
    return userController.updateUser()


@userRoute.route('/auth', methods=['POST'])
def loginUser():
    return userController.loginUser()
