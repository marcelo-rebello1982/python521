#!/usr/bin/env python3
import flask
from blueprints.api_routes import api

# __name__ // funcao implicita para retornar o nome da aplicaca
app = flask.Flask(__name__)
app.register_blueprint(api)
# app.run()
# app.run(port=80)


@app.route('/')
def index():
    return "Bem vindo, forasteiro"


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    return"<h5> Bem vindo a Area de cadastro</h5>>"




app.run(debug=True)
