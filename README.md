# Flask
Databases (still using docker)


10 steps to heaven ;)


1. Install Docker

2. Python 3.6.7 recommended

3. cd to Flask/docker_database/dockerized

4. Build docker container
> docker-compose up --build -d

Optional: (create virtual environment)

5. 
> pip install -r requirements.txt

6.
> pip install -r requirements2.txt

7. 
> cd to Flask/docker_database/dockerized/src

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
open config.py in visual studio -> 

change *user* and *password* to YOUR pgadmin-credentials in the 

DATABASE_URI="postgresql//:{user}:{password}/localhost:5432/soccer"
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

9. 
Windows Powershell: 
> $env:FLASK_APP = "app.py" 

Linux: 
> export FLASK_APP = "app.py"

10.
> flask run
