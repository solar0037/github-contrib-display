python3 -m pip install virtualenv
python3 -m virtualenv .venv
. .venv/bin/activate
python3 -m pip install -U pip
python3 -m pip install -r requirements.txt
deactivate
