# Web Dev Exercise #

requiremnts
- python 3.6 (or above)
- docker and docker-compose
- Flask

## Web & Logic ##

##### Logic (calculate next state) #####

to run the logic as a web service simply run `python server.py`
the service will bind to default port 5000 on local host (can be changed by providing `FLASK_PORT` ENV)
E.g of an input to the server using curl:
`curl http://localhost:5000/calculate -X POST -H 'content-type: application/json' -d '{"calculatorState": null, "input": "1"}'`

##### Server #####
run `docker-compose up backend` (the server will bind to localhost:8080)

## Tests ##

##### test (unitest) #####
run `python calculator_test.py`

##### test (integration tests) #####
run `python server_test.py`

##### e2e tests #####
run `docker-compose up e2e-test`



