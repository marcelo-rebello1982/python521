import os

import jenkins
import flask
import dotenv

dotenv.load_dotenv()

jenkins_routes = flask.Blueprint(
    name='jenkins', import_name=__name__, url_prefix='/jenkins')

user = os.getenv('JENKINS_USER')
passwd = os.getenv('JENKINS_PASSWORD')
server = os.getenv('JENKINS_SERVER')

# http://localhost:5000/jenkins/

# naveador : 
@jenkins_routes.route('/')
def index():
    try:
        client = jenkins.Jenkins(url=server, username=user, password=passwd)
        jobs_list = client.get_jobs()

        jobs = []

        for job in jobs_list:
            jobs.append(client.get_job_info(job['fullname']))
    except Exception as e:
        print(e)
        jobs = []
    finally:
        return flask.render_template('jenkins.html', jobs=jobs)

# nagevador : 
@jenkins_routes.route('/build/<string:job_name>')
def jenkins_build(job_name):
    try:
        client = jenkins.Jenkins(url=server, username=user, password=passwd)
        print('Olá mundo')
        client.build_job(job_name)
    except Exception as e:
        print(e)
        exit(1)
    except requests.exceptions.HTTPError:
        pass
    finally:
        return flask.redirect(flask.url_for('jenkins.index'))

# navegador : http://127.0.0.1:5000/jenkins/update/Meu%20deploy
@jenkins_routes.route('/update/<string:job_name>')
def jenkins_update(job_name):
    try:
        client = jenkins.Jenkins(url=server, username=user, password=passwd)
        job = {
            'name': job_name,
            'xml': client.get_job_config(job_name)
        }
    except Exception as e:
        print(e)
        exit(1)
    return flask.render_template('jenkins_update.html', job=job)

# navegador : 
@jenkins_routes.route('/rebuild', methods=['POST'])
def jenkins_rebuild(job_name):
    data = flask.request.form
    try:
        client = jenkins.Jenkins(url=server, username=user, password=passwd)
        client.reconfig_job(data['name'], data['xml'])
        return flask.redirect(flask.url_for('jenkins.index'))
    except Exception as e:
        return flask.redirect(flask.url_for('jenkins.update', job_name=data['name']))
