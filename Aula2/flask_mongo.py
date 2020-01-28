#!/usr/bin/env python3

import flask
import pymongo
from bson.json_util import dumps

app = flask.Flask(__name__)
client = pymongo.MongoClient()

db = client.app


@app.route('/')
def index():
    users = db.usuarios.find()

    # aqui nao pode esuecer o tipo de retorno neste metodo
    return flask.Response(dumps(users), status=200, content_type="application/json")
      
   # return flask.jsonify(dumps(users)) abaixo usar outro tipo de retornr, o response
   # return flask.Response(dumps(users), status=200, content_type="application/xml")

@app.route('/nome/<nome>')
def get_nome(nome):
    user = db.usuarios.find_one(
        {
            "nome": nome
        }
    )
    return flask.Response(dumps(user), status=200, content_type="application/json")


# @app.route('/delete/<username>')
# def delete_user(username):

#     deleted_user = db.usuarios.delete_one(
#         {
#             "nome": username

#         }
#     )

#     if delete_user.deleted_count == 0:
#         return "Uusario não encontrado"
#     else:
#         return f"Usuario {username}, deletado com sucesso"

@app.route('/delete/<username>')
def delete_user(username):
    try:
        deleted_user = db.usuarios.delete_one(
            {
                "nome": username
            }
        )
        assert deleted_user.deleted_count == 1, 'usuário não encontrado'
        return flask.jsonify(
            {
                "status": f' Usuário {username} deletado com sucesso'
            }
        )
    except pymongo.errors.ConnectionFailure:
        return "Reveja os dados de conexão com o banco"


app.run(debug=True)


# chamar as rotas pelo navegador
# http://127.0.0.1:5000/nome/Marcelo%20Paulo

# http://127.0.0.1:5000/delete/Marcelo%20Paulo

# listar os usuários
# http://127.0.0.1:5000/

# listar o usario por nome
# http://127.0.0.1:5000/nome/Davi%20Augusto

# não esquecer do retorno no metido acima, 

# deletar o usuario
# http://127.0.0.1:5000/delete/Joao%20Carlos

