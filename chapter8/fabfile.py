import os

from fabric.api import local
from fabric.decorators import task
from fabric.context_managers import settings, hide, cd, prefix
from fabric.operations import sudo, run, put
from fabric.state import env

circus_file_path = os.path.realpath('deploy/circus.ini')
circus_upstart_file_path = os.path.realpath('deploy/circus.conf')
nginx_config_path = os.path.realpath('deploy/nginx')
nginx_avaliable_path = "/etc/nginx/sites-available/"
nginx_enable_path = "/etc/nginx/sites-enabled/"
app_path = "~"
virtual_env_path = "~/py35env/bin/activate"

env.hosts = ['10.211.55.26']
env.user = 'phodal'
env.password = '940217'


@task
def install():
    """Install requirements packages"""
    local("pip install -r requirements/dev.txt")


@task
def runserver():
    """Run Server"""
    local("./manage.py runserver")


@task
def pep8():
    """ Check the project for PEP8 compliance using `pep8` """
    with settings(hide('warnings'), warn_only=True):
        local('pep8 .')


@task
def tag_version(version):
    """Tag New Version"""
    local("git tag %s" % version)
    local("git push origin %s" % version)


@task
def fetch_version(version):
    """Fetch Git Version"""
    local('wget https://codeload.github.com/phodal/growth_studio/tar.gz/%s' % version)


@task
def test():
    """ Run Test """
    local("./manage.py test blog")


@task
def e2e():
    """Run E2E Test"""
    local("./manage.py test e2e")


@task
def prepare_ac():
    run('echo "from django.contrib.auth.models import User; User.objects.create_superuser(%s, %s, %s)" | python manage.py shell' % ('test', 'test@phodal.com', 'test'))


@task
def ac():
    """Run E2E Test"""
    local("./manage.py test ac")


@task
def host_type():
    run('uname -a')


@task
def setup():
    """ Setup the Ubuntu Env """
    sudo('apt-get update')
    APT_GET_PACKAGES = [
        "build-essential",
        "git",
        "python3-dev",
        "python3-pip",
        "nginx",
        "virtualenv",
    ]
    sudo("apt-get install -y " + " ".join(APT_GET_PACKAGES))
    sudo('pip3 install circus')
    sudo('rm ' + nginx_enable_path + 'default')
    run('virtualenv --distribute -p /usr/bin/python3.5 py35env')


def nginx_restart():
    "Reset nginx"
    sudo("service nginx restart")


def nginx_start():
    "Start nginx"
    sudo("service nginx start")


def nginx_config(nginx_config_path=nginx_config_path):
    "Send nginx configuration"
    for file_name in os.listdir(nginx_config_path):
        put(os.path.join(nginx_config_path, file_name), nginx_avaliable_path, use_sudo=True)


def circus_config():
    "Send Circus configuration"
    sudo('mkdir -p /etc/circus/')
    put(circus_file_path, '/etc/circus/', use_sudo=True)


def circus_upstart_config():
    "Send Circus Upstart configuration"
    put(circus_upstart_file_path, '/etc/init/', use_sudo=True)


def circus_start():
    "Send Circus Upstart configuration"
    sudo('/usr/local/bin/circusd /etc/circus/circus.ini --daemon')
    sudo('circusctl restart')


def nginx_enable_site(nginx_config_file):
    "Enable nginx site"
    with cd(nginx_enable_path):
        sudo('rm -f ' + nginx_config_file)
        sudo('ln -s ' + nginx_avaliable_path + nginx_config_file)


@task
def deploy(version):
    """ depoly app to cloud """
    with cd(app_path):
        get_app(version)
        setup_app(version)
        config_app()

    nginx_config()
    nginx_enable_site('growth-studio.conf')

    circus_config()
    circus_upstart_config()

    circus_start()

    nginx_restart()


def config_app():
    with cd('growth-studio'):
        with prefix('source ' + virtual_env_path):
            run('python manage.py collectstatic -l --noinput')
            run('python manage.py migrate')


def setup_app(version):
    with prefix('source ' + virtual_env_path):
        run('pip3 install -r growth-studio-%s/requirements/prod.txt' % version)
        run('rm -f growth-studio')
        run('ln -s growth-studio-%s growth-studio' % version)


def get_app(version):
    run(('wget ' + 'https://codeload.github.com/phodal/growth_studio/tar.gz/v' + '%s') % version)
    run('tar xvf v%s' % version)
