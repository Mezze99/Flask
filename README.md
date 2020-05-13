# Flask
Databases


Servus,

to open pls start docker_database in venv/virtualenv on your local machine

you need docker preinstalled on ur machine

edit config.pi: in DATABASE_URI enter your postgresql credentials

in /dockerdb run:

docker-compose up --build -d

in /src run:
Linux: export FLASK_APP=app.py
Windows: 

set FLASK_APP=app.py
flask run

you can now find successful on localhost/5000
