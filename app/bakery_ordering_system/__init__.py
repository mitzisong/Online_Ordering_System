from flask import Flask
import os
import config
 
app = Flask(__name__)
app.config.from_object(config)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'mitzisong@gmail.com'
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')
 
from routes import mail
mail.init_app(app)

import bakery_ordering_system.routes