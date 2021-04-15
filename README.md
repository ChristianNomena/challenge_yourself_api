# challenge_yourself_api
The official API for Challenge Yourself App
It is an API made with Flask
ORM : SQLAlchemy

# database
You should create the database if it's not inside your server
The tables will be created automatically once you run the API
SGBD : MySQL
Database Name : challenge_yourself

# requirements
You can find all the libraries you need to start the API in the file "requirements.txt"

# run
Execute the "main.py" file to run the API

# models
The models represent the structures in database
We can manipulate the models to make operations and not with SQL requests

# routes
The routes are made for API operations (GET/POST/PUT/DELETE)

### User
GET /users : Get users list ---
GET /users/{userID} : Get specific user information ---
POST /users : Create an user with body {'pseudo': pseudo, 'mail': mail, 'password': password} ---
DELETE /users/{userID} : Delete an user
