from fabric.api import local
from fabric.decorators import task
from fabric.context_managers import settings, hide
from fabric.operations import sudo, run


@task
def install():
    """Install requirements packages"""
    local("pip install -r requirements.txt")


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
    local("./manage.py test")


@task
def setup():
    """ Setup the Ubuntu Env """
    sudo('apt-get update')
    APT_GET_PACKAGES = [
        "build-essential",
        "git",
        "python3-dev",
        "python3-virtualenv",
        "python3-pip",
        "nginx",
        "virtualenv",
    ]
    sudo("apt-get install " + " ".join(APT_GET_PACKAGES))
    sudo('pip3 install virtualenv')
    run('virtualenv --distribute -p /usr/bin/python3.5 py35env')


@task
def deploy(version):
    """ depoly app to cloud """
    run('cd ~/')
    run(('wget ' + 'https://codeload.github.com/phodal/growth_studio/tar.gz/v' + '%s') % version)
    run('tar xvf v%s' % version)

    # run('rm -rf growth-studio')
    # run('mv growth-studio-%s growth-studio'%version)
    # run('rm v%s'%version)

    run('source py35env/bin/activate')
    run('pip3 install -r growth-studio-%s/requirements/prod.txt' % version)
    run('ln -s growth-studio-%s growth-studio' % version)
