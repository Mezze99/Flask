# Flask
Databases (still using docker)

1. 
Install Docker

2. 
Python 3.6.7 recommended

3. 
cd to Flask/docker_database/dockerized

4. 
> docker-compose up --build -d

Optional: (create virtual environment)

5. 
> pip install -r requirements.txt

6.
> pip install -r requirements2.txt

7. 
> cd to Flask/docker_database/dockerized/src

8. 
Windows Powershell: 
> $env:FLASK_APP = "main.py" 

Linux: 
> export FLASK_APP = "main.py"

9.
> flask run
