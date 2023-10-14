from config.route_middleware import app
from flask import render_template, make_response

@app.errorhandler(404)
def error_404(error):
    return make_response(render_template('error_404.html', error = error), 404)

@app.errorhandler(500)
def error_500(error):
    return make_response(render_template('error_500.html', error = error), 500)
