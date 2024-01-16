# Web-Service_for_Tourism, Ethiopian cities

This project is done to get a wider knowlwdge on Python's Flask framework. The idea behind it is to simply serve a service where it displays tourist sites in specific cities of Ethiopia, It also allows users to add cities and tourist sites into the database which can make the database rich in information and can be reached where the author couldn't reach.

## Installation

### Dependencies

To be able to use this app we will need to have python version 3.6 or above with the following packages installed

- Flask - Framework for the API and serving of the frontend display
- Flask-cors - To allow requests from the same server
- SqlAlchemy - For the database ORM
- cmd - For the console interface

To install all this using the python package manager(pip) we will use the following command:-
`pip install flask-cors cmd sqlalchemy flask`

### Execution

Executing this app will be done with the following code.

- Browse to the main directory and run the following code on the first terminal
  `python3 app/app.py`, this will run the frontend
- On a different terminal run
  `python3 api/v1/app.py`, this will spin up the backend

## Environmental variables

| VARIABLE     | VALUES      | Meaning                                                     |
| ------------ | ----------- | ----------------------------------------------------------- |
| STORAGE_TYPE | db or other | db - use a database storage, any other - use a file storage |

## Improvment that are being worked on

- Authentication system to filter who can add information to the database
- Better CSS to make it look more appealing

## Authors

| Name               | email                     | github                            |
| ------------------ | ------------------------- | --------------------------------- |
| Birhan Kassaye     | birhanyalew2019@gmail.com | https://github.com/birhan-kassaye |
| Messai Hailemariam | messai.h.m@gmail.com      | https://github.com/hmmessai       |
