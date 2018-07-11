# Web Dev Exercise #

requiremnts
- python 3.6 (or above)
- docker and docker-compose

## Web & Logic ##

##### Logic (calculate next state) #####
run `python logic/calculator.py`

##### Server #####
run `docker-compose up backend` (the server will bind to localhost:8080)

## Tests ##

##### test (unitest) #####
run `python logic/calculator_test.py`

##### test (integration tests) #####
run `python logic/server_test.py`

##### e2e tests #####
run `docker-compose up e2e-test`



