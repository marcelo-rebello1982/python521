import os

import flask
import docker
# http://127.0.0.1:5000/docker/

docker_routes = flask.Blueprint(
    name='docker',
    import_name=__name__,
    url_prefix='/docker'
)

# BwT-JAzyLYG-xvhn9EJF


@docker_routes.route('/')
def index():
    if 'logged' in flask.session and flask.session['logged']:
        return flask.redirect(flask.url_for['ldap.index'])
    try:
        client = docker.from_env()
        container = client.containers.get('eca409ea8506')
        flask_app = {
            'id': container.short_id,
            'imagem': container.image.tags[0],
            'nome': container.name,
            'status': container.status
        }
    except Exception as e:
        flask_app = {}

    finally:
        return flask.render_template('docker.html', container=flask_app)


@docker_routes.route('/start')
def start():
    try:
        client = docker.from_env()
        container = client.containers.get('eca409ea8506')
        container.start()
    except Exception as e:
        print(e)
    return flask.redirect(flask.url_for('docker.index'))


@docker_routes.route('/stop')
def stop():
    try:
        client = docker.from_env()
        container = client.containers.get('eca409ea8506')
        container.stop()
    except Exception as e:
        print(e)
    return flask.redirect(flask.url_for('docker.index'))


@docker_routes.route('/restart')
def restart():
    try:
        client = docker.from_env()
        container = client.containers.get('eca409ea8506')
        container.restart()
    except Exception as e:
        print(e)
    return flask.redirect(flask.url_for('docker.index'))


@docker_routes.route('/ls')
def ls():
    print(os.system('ls /home/developer'))
    return flask.redirect(flask.url_for('docker.index'))
