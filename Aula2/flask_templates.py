#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():

    dados = {'title': 'Titulo Jinja',
             'cabecalho': 'Eu sei programar', 'botao': False
             }
    # return flask.render_template('index.html', dados=dados)
    # return flask.render_template('modelo.html')
    return flask.render_template('principal.html')


#  return flask.render_template('index.html', title='Titulo jinja',cabecalho='eu sei programar', botao=False)
app.run(debug=True)
