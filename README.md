# Flask
Databases - Project
by Tim Kauer, Sven Metzger and Georg Schieck


10 steps to heaven ;)


1. Install Docker

2. Python 3.6.8 recommended

3. cd to Flask/docker_database/dockerized

4. Build docker container
> docker-compose up --build -d

Optional: (create virtual environment)

5. Install dependencies 
> pip install -r requirements.txt

6.
> pip install -r requirements2.txt

7. 
> cd to Flask/docker_database/dockerized/src

8.1
Open pgadmin and create a new database and name it "soccer"

8.2
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
