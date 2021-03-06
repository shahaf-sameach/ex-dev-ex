# Web Dev Exercise #

requirements:
- python 3.6 (or above)
- docker and docker-compose
- Flask

## Web & Logic ##

##### Logic (calculate next state) #####

to run the logic as a web service simply run `python server.py`
the service will bind to default port 5000 on local host (can be changed by providing `FLASK_PORT` ENV)

e.g. of an input to the server using curl:
`curl http://localhost:5000/calculate -X POST -H 'content-type: application/json' -d '{"calculatorState": null, "input": "1"}'`

##### Server #####
- run `docker build . -t server`
- run `docker run -p 5000:5000 server`

##### Docker-compose #####
- run `docker-compose build`
- run `docker-compose up backend` (the server will bind to localhost:8080)

## Tests ##

##### Unit tests #####
run `python calculator_test.py`

##### Integration tests #####
run `python server_test.py`

##### E2E tests #####
The E2E tests are executed on a Firefox browser.

run `docker-compose up e2e-test`



