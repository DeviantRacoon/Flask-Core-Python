from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

def setConfig(app, env):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{env['USER_DATABASE']}:{env['PASSWORD_DATABASE']}@{env['HOST_DATABASE']}:{env['PORT_DATABASE']}/{env['DATABASE']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)
# engine = create_engine(f"mysql+pymysql:/{env['USER_DATABASE']}:{env['PASSWORD_DATABASE']}@{env['HOST_DATABASE']}:{env['PORT_DATABASE']}/{env['DATABASE']}")
