from flask import Flask
from flask_cors import CORS
from .database import setConfig
from .dotenv import env
from modules.core.infrastructure.routes import person_route, user_route
from .jwt import setConfigJWT

app = Flask(env['NAME_APP'], template_folder = 'app/modules/core/infrastructure/templates')
CORS(app, resources={r"*": {"origins": env['CROSS_ORIGIN']}})

setConfig(app, env)
jwt = setConfigJWT(app, env)

app.register_blueprint(person_route.personRoute)
app.register_blueprint(user_route.userRoute)