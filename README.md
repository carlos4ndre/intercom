![Travis build](https://travis-ci.com/carlos4ndre/intercom.svg?branch=master)


Intercom Code Challenge
=======================

### Technical problem

We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted.

We want to invite any customer within 100km of our Dublin office for some food and drinks on us.

Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

You must use the first formula from this Wikipedia article to calculate distance. Don't forget, you'll need to convert degrees to radians.

The GPS coordinates for our Dublin office are 53.339428, -6.257664.

### Solution

* Used repository pattern to abstract the data source, which currently is a plain text file with all customer data, this will allow for easier transition into a database
* Used type hint for reducing type mistakes
* Added security checks
* Added unit and integration tests
* Added simple CI/CD job for running the tests on travis
* Run the script in Docker for better portability

### Requirements

* Python 3.7.x
* Tox 3.x
* Docker

### Run tests

$ make test

### Run script

$ make build
$ make run
