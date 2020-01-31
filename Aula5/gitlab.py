#!/usr/bin/env python3

import requests
import json

private_token = "BwT-JAzyLYG-xvhn9EJF"
url = 'http://192.168.200.172/api/v4/'

payload = {"private_token": private_token}

# listaggem dos projetos

projetos = requests.get(url + 'projects', params=payload)

# print(projetos.url)
# print(json.dumps(projetos.json(), indent=4))

payload = {
    'name': 'flask-app'
}

# projeto = requests.post(url + 'projects?private_token=' + private_token, payload)
# print(json.dumps(projeto.json(), indent=4))
