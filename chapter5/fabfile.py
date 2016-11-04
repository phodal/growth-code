from fabric.api import local
from fabric.decorators import task
from fabric.context_managers import settings, hide


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
    local("git push origin %s"%version)


@task
def fetch_version(version):
    """Fetch Git Version"""
    local('wget https://codeload.github.com/phodal/growth_studio/tar.gz/%s'%version)


@task
def test():
    """ Run Test """
    local("./manage.py test")

