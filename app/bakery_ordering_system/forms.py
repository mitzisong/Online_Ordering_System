from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField, ValidationError

 
class ContactForm(Form):
    name = TextField("Name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address.")])
    subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")

class SignupForm(Form):
    firstname = TextField("First name", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name", [validators.Required("Please enter your last name.")])
    phonenumber = TextField("Phone number", [validators.Required("Please enter your phone number.")])
    email = TextField("Email", [validators.Required("Please enter your email address.")])
    submit = SubmitField("Continue")

    # def __init__(self, *args, **kwargs):
    #     Form.__init__(self, *args, **kwargs)

    # def validate(self):
    #     if not Form.validate(self):
    #         return False

class DeliveryRecipientForm(Form):
    name = TextField("Name", [validators.Required("Please enter recipient's name.")])
    phonenumber = TextField("Phone number", [validators.Required("Please enter recipient's phone number.")])
    companyname = TextField("Company Name (if applicable)")
    streetaddress = TextField("Street Address", [validators.Required("Please enter your street address.")])
    unit = TextField("Unit")
    city = TextField("City", [validators.Required("Please enter your city.")])
    state = TextField("State", [validators.Required("Please enter your state.")])
    zipcode = TextField("Zip Code", [validators.Required("Please enter your zip code.")])

    # def __init__(self, *args, **kwargs):
    #     Form.__init__(self, *args, **kwargs)

    # def validate(self):
    #     if not Form.validate(self):
    #         return False

class ChooseCupcakesForm(Form):
    submit = SubmitField("Continue")