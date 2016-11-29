# Setup a proper path, I call my virtualenv dir "venv" and
# I've got the virtualenv command installed in /usr/local/bin
PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv" ]; then
  virtualenv --distribute -p /usr/local/bin/python3.5 py35env
fi
. py35env/bin/activate
