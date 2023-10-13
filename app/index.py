from flask import render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from config.route_middleware import env, app
from config.database import database as db
from config.logging import logger


@app.route('/')
def index():
    # return make_response(render_template('index.html', title = env['NAME_APP']), 200)
    return {"ok": True, "message": "Se pudo"}

@app.errorhandler(404)
def error_404(error):
    return make_response(render_template('error_404.html', error = error), 404)

@app.errorhandler(500)
def error_404(error):
    return make_response(render_template('error_500.html', error = error), 500)

with app.app_context():
    logger(db.create_all)


if __name__ == '__main__':
    app.run(debug=env['DEBUG'], host=env['HOST'], port=env['PORT'])