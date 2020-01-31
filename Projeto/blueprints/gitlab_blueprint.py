import flask
import requests

gitlab_routes = flask.Blueprint(
    'gitlab', import_name=__name__, url_prefix='/gitlab')

token = 'BwT-JAzyLYG-xvhn9EJF'

# http://127.0.0.1:5000/gitlab/
# no navegador http://127.0.0.1:5000/gitlab/
@gitlab_routes.route('/')
def index():
    usuarios = requests.get(
        'http://192.168.200.172/api/v4/users?private_token=' + token).json()

    return flask.render_template('gitlab.html', users=usuarios)
