#!/usr/bin/env python3

import requests as r

# requisicoes do tipo get


# url_api = 'http://gen-net.herokuapp.com/api/users'

cep = '12420060'

url_api = "https://viacep.com.br/ws/01001000/json/".format(cep)

res = r.get(url_api)
assert res.status_code == 200, 'Não consegui chegar na pagina'
# print(res.__dir__()) # // mostra todos os parametros do objeto
# print(dir(res))
# print(res.json())

usuarios = res.json()
endereco = res.json()
# print('tipo de usuarios  : ' , type(usuarios))
# print('tipo de enderecos :', type(endereco))
# print('chaves do dicionario : ', type(endereco))
# print(type (usuarios))
# print(len(usuarios))

print('metodos : ', usuarios.__dir__())

for dados in endereco:
    print('dados json : ', dados)


print('status code : ', res.status_code)

# print('CEP : ', endereco['cep'])
# print('logradouro : ' , endereco['logradouro'])
# print('Cidade: {}-{}'.format(endereco['localidade'].endereco['uf']))

cep2 = input('digite seu cep: ')
url_api2 = f'https://viacep.com.br/ws/{cep2}/json/'  # 12412-010
res2 = r.get(url_api2)
# print(res2)
endereco2 = res2.json()

# print('endereco 2' , endereco2)


# cadastrar um usuario na API

# so chamar nome, email e senha que cadastra :

def cadastra(nome: str, email: str, password: str) -> int:
    '''
    para cadastrar usuarios na api só chamar com o nome e senha que cadastra
    '''

    dados = {
        'name': nome,
        'email': email,
        'password': password
    }

    res = r.post('https://gen-net.herokuapp.com/api/users', data=dados)

    print(res.json())
    assert res.status_code == 200
    return res.json()['id']


def ler_usuario(id):
    res = r.get(f'https://gen-net.herokuapp.com/api/users/{id}')
    return res.json()


def ler_usuario2(id: int) -> dict:
    res = r.get(f'https://gen-net.herokuapp.com/api/users/{id}')
    return res.json()


def ler_usuario3(id: int):
    res3 = r.get(f'https://gen-net.herokuapp.com/api/users/{id}')
    return res3.json()


# print('id : ', res.json()[0]['id'])
# print(cadastra('Marcelo 4', 'mp.rebello.martins4@gmail.com', '66325'))
# print(ler_usuario2(319))
# print(ler_usuario3(319))

res4 = r.get(f'https://gen-net.herokuapp.com/api/users/{319}')
res5 = res4.json()
print(res5)

