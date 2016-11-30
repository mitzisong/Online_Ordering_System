import os

# Config file, put all your keys and passwords and whatnot in here
SECRET_KEY = "this should be a secret"

# Default to sqlite db unless the environment has a DATABASE_URI set
#  (heroku will set this for us when we run on there)
<<<<<<< HEAD
DB_URI = os.environ.get("DATABASE_URI", "postgres://mitzisong@localhost:5432/bakery")
=======
DB_URI = os.environ.get("DATABASE_URI", "postgres://localhost/bakery")
>>>>>>> 2961bf400535b735ad183cc7c54e3240df727fbc
