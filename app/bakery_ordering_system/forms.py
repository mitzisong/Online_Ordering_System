<<<<<<< HEAD
from flask_wtf import Form
=======
from flask.ext.wtf import Form
>>>>>>> 2961bf400535b735ad183cc7c54e3240df727fbc
from wtforms import TextField, SelectField, RadioField, SubmitField, validators, TextAreaField, ValidationError

 
class ContactForm(Form):
    name = TextField("Name*",  [validators.Required("Please enter your name.")])
    email = TextField("Email*",  [validators.Required("Please enter your email address.")])
    subject = TextField("Subject*",  [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message*",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")

class SignupForm(Form):
    firstname = TextField("First name*", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name*", [validators.Required("Please enter your last name.")])
    phonenumber = TextField("Phone number*", [validators.Required("Please enter your phone number.")])
    email = TextField("Email*", [validators.Required("Please enter your email address.")])
    day = SelectField("What day would you like your cupcakes?", choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"), ("13", "13"), ("14", "14"), ("15", "15"), ("16", "16"), ("17", "17"), ("18", "18"), ("19", "19"), ("20", "20"), ("21", "21"), ("22", "22"), ("23", "23"), ("24", "24"), ("25", "25"), ("26", "26"), ("27", "27"), ("28", "28"), ("29", "29"), ("30", "30"), ("31", "31")])
    month = SelectField("What month would you like your cupcakes?", choices=[("jan", "January"), ("feb", "February"), ("mar", "March"),  ("apr", "April"), ("may", "May"), ("jun", "June"), ("jul", "July"), ("aug", "August"), ("sep", "September"), ("oct", "October"), ("nov", "November"), ("dec", "December")])
    year = SelectField("What year would you like your cupcakes?", choices=[("2014", "2014"), ("2015", "2015"), ("2016", "2016"), ("2017", "2017"), ("2018", "2018"), ("2019", "2019"), ("2020", "2020"), ("2021", "2021")])
    time = SelectField("What time would you like your cupcakes?", choices=[("10:00", "10:00am"), ("10:30", "10:30am"), ("11:00", "11:00am"), ("11:30", "11:30am"), ("12:00", "12:00pm"), ("12:30", "12:30pm"), ("13:00", "1:00pm"), ("13:30", "1:30pm"), ("14:00pm", "2:00pm"), ("14:30", "2:30pm"),("15:00", "3:00pm"), ("15:30", "3:30pm"), ("16:00", "4:00pm"), ("16:30", "4:30pm"), ("17:00", "5:00pm"), ("17:30", "5:30pm")])
    submit = SubmitField("Continue")

    # def __init__(self, *args, **kwargs):
    #     Form.__init__(self, *args, **kwargs)

    # def validate(self):
    #     if not Form.validate(self):
    #         return False

class DeliveryRecipientForm(Form):
    altname = TextField("Name")
    altphonenumber = TextField("Phone number")
    companyname = TextField("Company Name (if applicable)")
    streetaddress = TextField("Street Address*", [validators.Required("Please enter your street address.")])
    unit = TextField("Unit")
    city = TextField("City*", [validators.Required("Please enter your city.")])
    state = TextField("State*", [validators.Required("Please enter your state.")])
    zipcode = TextField("Zip Code*", [validators.Required("Please enter your zip code.")])
    deliverymethod = RadioField("delivery", choices=[("True", "Pick-Up"), ("False", "Delivery $25")], coerce=unicode)

    # def __init__(self, *args, **kwargs):
    #     Form.__init__(self, *args, **kwargs)

    # def validate(self):
    #     if not Form.validate(self):
    #         return False

# class ChooseCupcakesForm(Form):
#     quantity = TextField("How many dozen would you like?")
#     submit = SubmitField("Continue")

class ChooseDecorationsForm(Form):
    decoration = SelectField("What decoration theme would you like?", choices=[("signature", "Signature"), ("festive", "Festive"), ("birthday", "Birthday"), ("babyshower", "Baby Shower"), ("bridalshower", "Bridal Shower"), ("animals", "Animals"), ("underthesea", "Under the Sea"), ("sports", "Sports"), ("49ers", "49ers"), ("sfgiants", "SF Giants"), ("newyears", "New Years"), ("valentinesday", "Valentine's Day"), ("stpatricksday", "St. Patrick's Day"), ("easter", "Easter"), ("4thofjuly", "4th of July"), ("halloween", "Halloween"), ("thanksgiving", "Thanksgiving"), ("christmas", "Christmas")])
    color1 = SelectField("What color scheme would you like?", choices=[("red", "Red"), ("orange", "Orange"), ("pastelorange", "Pastel Orange"), ("yellow", "Yellow"), ("pastelyellow", "Pastel Yellow"), ("green", "Green"), ("pastelgreen", "Pastel Green"), ("turquoise", "Turquoise"), ("pastelturquoise", "Pastel Turquoise"), ("blue", "Blue"), ("pastelblue", "Pastel Blue"), ("purple", "Purple"), ("lavender", "Lavender"),  ("pink", "Pink"), ("pastelpink", "Pastel Pink"), ("hotpink", "Hot Pink"), ("brown", "Brown"), ("grey", "Grey"), ("black", "Black"), ("white", "White")])
    color2 = SelectField("What color scheme would you like?", choices=[("none", "None"), ("red", "Red"), ("orange", "Orange"), ("pastelorange", "Pastel Orange"), ("yellow", "Yellow"), ("pastelyellow", "Pastel Yellow"), ("green", "Green"), ("pastelgreen", "Pastel Green"), ("turquoise", "Turquoise"), ("pastelturquoise", "Pastel Turquoise"), ("blue", "Blue"), ("pastelblue", "Pastel Blue"), ("purple", "Purple"), ("lavender", "Lavender"),  ("pink", "Pink"), ("pastelpink", "Pastel Pink"), ("hotpink", "Hot Pink"), ("brown", "Brown"), ("grey", "Grey"), ("black", "Black"), ("white", "White")])
    color3 = SelectField("What color scheme would you like?", choices=[("none", "None"), ("red", "Red"), ("orange", "Orange"), ("pastelorange", "Pastel Orange"), ("yellow", "Yellow"), ("pastelyellow", "Pastel Yellow"), ("green", "Green"), ("pastelgreen", "Pastel Green"), ("turquoise", "Turquoise"), ("pastelturquoise", "Pastel Turquoise"), ("blue", "Blue"), ("pastelblue", "Pastel Blue"), ("purple", "Purple"), ("lavender", "Lavender"),  ("pink", "Pink"), ("pastelpink", "Pastel Pink"), ("hotpink", "Hot Pink"), ("brown", "Brown"), ("grey", "Grey"), ("black", "Black"), ("white", "White")])
    submit = SubmitField("Continue")