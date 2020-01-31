#!/usr/bin/env python3

import docker

# client = docker.Docker('tcp://localhost:2376') so para conexao remota
try:
    client = docker.from_env()  # conexão local
except Exception:
    exit(1)


# Listar todos os containers
# print(client.containers.run('python', 'python3 --help'))
# print(client.containers.list())

for container in client.containers.list():
    #   print('lista : ', container.__dir__(), '\n')

    #   print(client.containers.run('ubuntu', 'bash',detach=True))

    container_ubuntu = client.containers.get('78f307803a')
    print(dir('container ubuntu : ', container_ubuntu))

    try:
        container_ubuntu.stop()
        print('Container parado...')
    except Exception as e:
        prin(e)
        

# http://dontpad.com/4linux

