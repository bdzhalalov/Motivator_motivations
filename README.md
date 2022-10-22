# Motivation API

This API is intended for services that want to provide users with the ability to motivate each other by writing motivation and then displaying it to all users.

## Dependencies

* Django 4.0.6
* MySQL 5.7.37
* Redis 6.0
* Celery 5.2.7

## Features

* This is REST API with the possibility to read, create, update and delete resources located in database.

* All parts of API are placed in docker containers and combined using a `docker-compose` file.

* Access to API is realized with API-key which is checked with custom `middleware`.

* It's possible to test API with tests that are avialable in it (standart `unittest` library or `pytest` library).

* Motivations from unregistered users are hidden, but become visible after 15 minutes due to the work of Celery.

* Redis is used as broker for tasks in Celery and cache backend for save `Etag` header for responses.

* `Etag` header allows to send a response with `304` status code if he matches with `If-none-match` header in request.

## Usage

You can use [Motivator_users](https://github.com/Bahch1k/Motivator_users) project or use Postman to test API.

Don't forget to create `.env` file to setup environment variables like `API-KEY` or variables to connect to the database.
