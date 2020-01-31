#!/usr/bin/env python3

import flask
from blueprints.docker_blueprint import docker_routes
from blueprints.jenkins_blueprint import jenkins_routes
from blueprints.ldap_blueprint import ldap_routes


app = flask.Flask(__name__)
app.secret_key= 'chave'

app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)
app.register_blueprint(ldap_routes)

# no navegador http://127.0.0.1:5000/login/
# python3 app.py 
# http://dontpad.com/521-4linux/

@app.route('/')
def index():
    return flask.render_template('index.html')
app.run(debug=True)





