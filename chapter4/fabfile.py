from fabric.api import local
from fabric.decorators import task

@task
def install():
    """Install requirements packages"""
    local("pip install -r requirements.txt")

@task
def runserver():
    """Run Server"""
    local("./manage.py runserver")
