from fabric.api import local

def install():
    local("pip install -r requirements.txt")