import os

# Config file, put all your keys and passwords and whatnot in here
SECRET_KEY = "this should be a secret"

# Default to sqlite db unless the environment has a DATABASE_URI set
#  (heroku will set this for us when we run on there)
DB_URI = os.environ.get("DATABASE_URI", "sqlite:///bakery.db")
