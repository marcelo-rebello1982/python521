#!/usr/bin/env python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['app']  # o app se referre ao banco banco
except Exception as e:
    print(e)

# usuario = db.usuarios.insert_one(
#     {
#         '_id': 21,
#         'nome': 'ZEZITO',
#         'sobrenome': 'ROBERTO'
#     }
# )

print(db.usuarios.find())
listaDeUsuarios = [x for x in db.usuarios.find()]
print(listaDeUsuarios)





# user = db.usuarios.update_one(
#     {
#         "nome": "Daniel",
#         "sobrenome": "Silva"

#     },
#     {
#         "$set": {
#             "nome": "Júlio"
#         }

#     }
# )

# assert user.modified_count == 1, "Não foram modificados registros"
# print("print 2", user.matched_count, user.modified_count)


deleted = db.usuarios.delete_one(

    {
        "nome": "Zezito"
    }

)

assert deleted.deleted_count == 1, "Não encontrou registros para apagar"

