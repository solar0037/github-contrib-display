python -m virtualenv .venv
call .venv\Scripts\activate
python -m pip install -U pip
python -m pip install -r requirements.txt
call deactivate
