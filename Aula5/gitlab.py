#!/usr/bin/env python3

import requests
import json

private_token = "BwT-JAzyLYG-xvhn9EJF"
url = 'http://192.168.200.172/api/v4/users?'
# "BwT-JAzyLYG-xvhn9EJF"

payLoad = {"private_token": private_token}

# listaggem dos projetos

projetos = requests.get(url + 'projects', params=payLoad)

# print(projetos.url)
# print(json.dumps(projetos.json(), indent=4))

payLoad = {
    'name': 'flask-app'
}

# listando projetos
# projeto = requests.post(url + 'projects?private_token=' + private_token, payLoad)
# print(json.dumps(projeto.json(), indent=4))


# listando usuarios
payLoad = {"private_token": private_token}
usuarios = requests.get(url + 'users', params=payLoad)

# print(json.dumps(usuarios.json(), indent=4))

# Aidiconando usuário

new_user = {
    'email': 'mp.rebello.martins2@gmail.com',
    'username': '"marcelo-rebello2',
    'name': 'Marcelo Rebello 2',
    'password': 'umaVezPalmeirense'

}

usuario = requests.post(url + 'users?private_token=' + private_token, new_user)

print(json.dumps(usuario.json(), indent=4))

# http://dontpad.com/4linux
