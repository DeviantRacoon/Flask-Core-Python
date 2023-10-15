from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database import setConfig
from .dotenv import env
from modules.core.infrastructure.routes import person_route, user_route
from .jwt import setConfigJWT

app = Flask(env['NAME_APP'], template_folder = 'app/modules/core/infrastructure/templates')

setConfig(app, env)
jwt = setConfigJWT(app, env)

app.register_blueprint(person_route.personRoute)
app.register_blueprint(user_route.userRoute)