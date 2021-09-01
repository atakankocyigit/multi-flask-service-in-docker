# Multi Flask Service in Docker
Using docker, we can run multiple services independently by separating them. In this way, you can use different packages in both services and avoid dependencies.
In the project, 2 independent flask applications were containerized and collected as independent services. In addition, nginx was used as the web server. While establishing nginx connection with Flask, uwsgi was used.

## Project Usage
It can be run with the command "docker-compose up --build" in the folder. In addition, the pages can be accessed via http://localhost:81/flask/ and http://localhost:81/flask2/ after the project is up and running.
