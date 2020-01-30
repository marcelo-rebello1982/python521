#!/usr/bin/env python3

import jenkins
# print(dir(jenkins))

try:
    client = jenkins.Jenkins('http://localhost:8080',
                             username='marcelo-rebello', password='915gavmn245')
except Exception as e:
    print('erro de conexao : ', e)


# pegar o nome do usuário logado na plataforma
user = client.get_whoami()
print(user['fullName'])

version = client.get_version()
print(version)


# pegar a quantidade de jobs ativos criados
print(client.jobs_count())


# criar jobs pelos xml's
# print(jenkins.EMPTY_CONFIG_XML)
# client.create_job('Job_vazio', jenkins.EMPTY_CONFIG_XML) // comentei porque já tinha o job criado
print(client.jobs_count())


# pegar configuracao de um job
try:
    client.get_job_config('job_vazio')
except Exception as e:
   # client.create_job('job_vazio', jenkins.EMPTY_CONFIG_XML)
    print(e)


# BUILD DE UM JOB
#client.build_job('Meu deploy 3')

# Desablitar um jon
#client.disable_job('meu job')

# deletar um job
#client.delete_job('job bazio')

# habilita um job
# client.enable_job

# desabilitar um job
# client.disable_job

# reconfigurar um job
#client.reconfig_job('job_vazio2', jenkins.RECONFIG_XML)

# copiar um job
#client.copy_job('job_vazio2', 'job_vazio')


# trabalhar com plugins
# print(client.get_plugin_info)

# print(client.get_plugins())


# pegar informacoes de um plugin especifico
print(client.get_plugin_info('Email Extension Plugin'))

# tempo para o jenkins estar preparadao
if client.wait_for_normal_op(30):
    print('Rodando normal')
else:
    raise Exception('Deu ruim')
