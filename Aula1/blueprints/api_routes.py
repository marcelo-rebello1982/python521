import flask

api = flask.Blueprint("api", __name__, url_prefix="/api")


@api.route('/')
def index():
    dados = {
        "nome": "Marcelo Paulo",
        "sobrenome": "Rebello Martins"
    }
    return flask.jsonify(dados)


@api.route('/users')
def users():
    return 'Listagem de usuarios aqui'
