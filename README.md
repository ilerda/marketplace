# marketplace
Simple REST API using flask

## Description
This simple REST API implements the basic CRUD operations to maintain a database of products.

The five provided functions are:
* GET /v1/products - index
* POST /v1/product/{product_id} - create
* GET /v1/product/{product_id} - retrieve
* PUT /v1/product/{product_id} - update
* DELETE /v1/product/{product_id} - delete

## Setup
First, you should activate the virtual environment by running:
. venv/bin/activate

Next, to start up the server you simply run:
python3 app.py

After doing this, you can use simple curl commands from the terminal to send sample HTTP requests.

There are also some unit tests in the tests folder which do effectively the same thing.

## To Do
For next steps, it would be good to properly integrate the files as a python package, with all the required boilerplate code.

This will make it possible to improve the unit tests, by using the recommended flask functions for testing. The current unit tests are a bit unstable.

Another task would be to create better documentation for by using the Swagger/OpenAPI recommendations.
