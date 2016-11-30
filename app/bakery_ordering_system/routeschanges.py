 from bakery_ordering_system import app, models
from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import ContactForm, SignupForm, DeliveryRecipientForm, ChooseDecorationsForm
from flask.ext.mail import Message, Mail
from models import Customer, Delivery_Recipient, Order_Product, Product, Order, session as dbsession
import datetime
import os
import stripe

mail = Mail()

# stripe_keys = {
#     'secret_key': os.environ['SECRET_KEY'],
#     'publishable_key': os.environ['PUBLISHABLE_KEY']
# }

# stripe.api_key = stripe_keys['secret_key']

# app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/menu')
def menu():
  return render_template('menu.html')

@app.route('/order', methods = ['GET', 'POST'])
def order():
  form = SignupForm(csrf_enabled=False)
  # print "DELIVERYMETHOD", request.form.get("deliverymethod")
  deliveryrecipientform = DeliveryRecipientForm(csrf_enabled=False)

  if request.method=="POST":
    if form.validate_on_submit():

    # print "DELIVERYMETHOD", deliveryrecipientform.deliverymethod.data
      if deliveryrecipientform.deliverymethod.data=="True":
        # print "I AM SET FOR PICK UP"
      elif deliveryrecipientform.deliverymethod.data=="False":
        # print "I AM SET FOR DELIVERY"
        if form.validate_on_submit():
          newuser = Customer(firstname = form.firstname.data, 
                             lastname  = form.lastname.data, 
                             phonenumber = form.phonenumber.data, 
                             email = form.email.data)
          dbsession.add(newuser)
          dbsession.commit()
          dbsession.refresh(newuser) #gets the id from the database
          newuser_id = models.session.query(Customer).order_by(Customer.id.desc()).first()
          # print "NEWUSER_ID", newuser_id.id

          if deliveryrecipientform.validate_on_submit():
            deliveryrecipient = Delivery_Recipient(customer_id = newuser_id.id,
                                                   altname = deliveryrecipientform.altname.data,
                                                   altphonenumber = deliveryrecipientform.altphonenumber.data,
                                                   companyname = deliveryrecipientform.companyname.data,
                                                   streetaddress = deliveryrecipientform.streetaddress.data,
                                                   unit = deliveryrecipientform.unit.data,
                                                   city = deliveryrecipientform.city.data,
                                                   state = deliveryrecipientform.state.data,
                                                   zipcode = deliveryrecipientform.zipcode.data)
            dbsession.add(deliveryrecipient)
            dbsession.commit()
            dbsession.refresh(deliveryrecipient)
          else:
            return render_template('order.html', form=form,
                                   deliveryrecipientform = deliveryrecipientform)

    else:
      return render_template('order.html', form=form,
                             deliveryrecipientform = deliveryrecipientform)

    deliveryrecipient_id = models.session.query(Delivery_Recipient).order_by(Delivery_Recipient.id.desc()).first()
    print "DELIVERY RECIPIENT ID", deliveryrecipient_id.id
    # print "This is the time", form.time.data
    # print "This is the day", form.day.data
    # print "This is the month", form.month.data
    # print "This is the year", form.year.data
    newcustomer_id = models.session.query(Customer).order_by(Customer.id.desc()).first()
    date_string = form.month.data + "-" + form.day.data + "-" + form.year.data
    my_date = datetime.datetime.strptime(date_string, "%b-%d-%Y")
    time_string = form.time.data
    date_time_string = date_string + " " + time_string
    my_date_time = datetime.datetime.strptime(date_time_string, "%b-%d-%Y %H:%M")
    # print my_date_time
    # print "DELIVERYMETHOD", deliveryrecipientform.deliverymethod.data
    # newuser_id = models.session.query(Customer)
    neworder = Order(customer_id = newcustomer_id.id,
                     recipients_id = deliveryrecipient_id.id,
                     date_time = my_date_time,
                     delivery = deliveryrecipientform.deliverymethod.data)

    dbsession.add(neworder)
    dbsession.commit()

    return redirect(url_for('order2'))
    # , order_id=neworder.id


  return render_template('order.html', form=form,
                                       deliveryrecipientform=deliveryrecipientform)

@app.route("/order2", methods=["GET"])
def show_cart():
  minis = models.session.query(Product).filter_by(size="Mini")
  regulars = models.session.query(Product).filter_by(size="Regular")
  return render_template('order2.html', minis_products = minis,
                                        reg_products = regulars)


@app.route('/order2', methods = ['POST'])
def process_cart():
  minis = models.session.query(Product).filter_by(size="Mini")
  regulars = models.session.query(Product).filter_by(size="Regular")

  neworder_id = models.session.query(Order).order_by(Order.id.desc()).first()
  whole_form = request.form
  for product_id in whole_form.iterkeys():
    #if there is an input
    if whole_form[product_id] != "":
      print "These cupcakes:", product_id, whole_form[product_id]

      new_order_product = Order_Product(order_id = neworder_id.id,
                                        product_id = int(product_id),
                                        quantity = float(whole_form[product_id]))
      dbsession.add(new_order_product)
      dbsession.commit()

  return redirect(url_for('order3'))


@app.route('/order3', methods = ['GET', 'POST'])
def order3():
  choosedecorationsform = ChooseDecorationsForm(csrf_enabled=False)
  colors = choosedecorationsform.color1.data+"/"+choosedecorationsform.color2.data+"/"+choosedecorationsform.color3.data

  if request.method=="POST":
    print choosedecorationsform.color1.data
    print "THESE ARE THE COLORS", colors 
    print choosedecorationsform.decoration.data
    neworder = models.session.query(Order).order_by(Order.id.desc()).first()
    neworder.decorationtheme = choosedecorationsform.decoration.data
    neworder.colorscheme = colors

    dbsession.commit()

    return redirect(url_for('orderreview'))

  return render_template('order3.html', choosedecorationsform=choosedecorationsform)

@app.route('/orderreview', methods = ['GET', 'POST'])
def orderreview():
  form = SignupForm(csrf_enabled=False)

  customer = models.session.query(Customer).order_by(Customer.id.desc()).first()
  # firstname = a.firstname
  # lastname = a.lastname
  # phonenumber = a.phonenumber
  # email = a.email

  b = models.session.query(Delivery_Recipient).order_by(Delivery_Recipient.id.desc()).first()
  # altname = b.altname
  # altphonenumber = b.altphonenumber
  # companyname = b.companyname
  # streetaddress = b.streetaddress
  # unit = b.unit
  # city = b.city
  # state = b.state
  # zipcode = b.zipcode

  c = models.session.query(Order).order_by(Order.id.desc()).first()
  # date_time = c.date_time
  # decorationtheme = c.decorationtheme
  # colorscheme = c.colorscheme
  # delivery = c.delivery

  d = models.session.query(Order_Product).filter_by(order_id=c.id).all()

  totalcost = 0;
  if c.delivery == False:
    totalcost = 25
  e = []
  for product in d:
    e.append(product)
    print "THIS IS THE PRODUCT QUANTITY", product.quantity
    totalcost += product.product.cost * product.quantity

  if request.method == "POST":
    return redirect(url_for('payment'))


  # e = models.session.query(Product).order_by(Product.id.desc()).first()
  # cost = e.cost  


  return render_template('confirmation.html', customer = customer,
                                              firstname = a.firstname,
                                              lastname = a.lastname,
                                              phonenumber = a.phonenumber,
                                              email = a.email,
                                              altname = b.altname,
                                              altphonenumber = b.altphonenumber,
                                              companyname = b.companyname,
                                              streetaddress = b.streetaddress,
                                              unit = b.unit,
                                              city = b.city,
                                              state = b.state,
                                              zipcode = b.zipcode,
                                              date_time = datetime.datetime.strftime(c.date_time, "%b-%d-%Y %H:%M"),
                                              decorationtheme = c.decorationtheme,
                                              colorscheme = c.colorscheme,
                                              products = e,
                                              totalcost = totalcost,
                                              delivery = c.delivery,
                                              form = form)

@app.route('/payment', methods = ['GET', 'POST'])
def payment():
  if request.method == "POST":
    return redirect(url_for('confirmation'))
  
  return render_template('payment.html')

@app.route('/confirmation')
def confirmation():
  a = models.session.query(Customer).order_by(Customer.id.desc()).first()
  firstname = a.firstname

  b = models.session.query(Delivery_Recipient).order_by(Delivery_Recipient.id.desc()).first()
  altname = b.altname
  altphonenumber = b.altphonenumber
  companyname = b.companyname
  streetaddress = b.streetaddress
  unit = b.unit
  city = b.city
  state = b.state
  zipcode = b.zipcode

  c = models.session.query(Order).order_by(Order.id.desc()).first()
  date_time = c.date_time
  decorationtheme = c.decorationtheme
  colorscheme = c.colorscheme
  delivery = c.delivery

  d = models.session.query(Order_Product).filter_by(order_id=c.id).all()

  totalcost = 0;
  if delivery == False:
    totalcost = 25
  e = []
  for product in d:
    e.append(product)
    print "THIS IS THE PRODUCT QUANTITY", product.quantity
    totalcost += product.product.cost * product.quantity

  return render_template('orderreview.html', firstname = a.firstname,
                                            lastname = a.lastname,
                                            phonenumber = a.phonenumber,
                                            email = a.email,
                                            altname = b.altname,
                                            altphonenumber = b.altphonenumber,
                                            companyname = b.companyname,
                                            streetaddress = b.streetaddress,
                                            unit = b.unit,
                                            city = b.city,
                                            state = b.state,
                                            zipcode = b.zipcode,
                                            date_time = datetime.datetime.strftime(c.date_time, "%b-%d-%Y %H:%M"),
                                            decorationtheme = c.decorationtheme,
                                            colorscheme = c.colorscheme,
                                            products = e,
                                            totalcost = totalcost,
                                            delivery = c.delivery)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm(request.form)
  if request.method == 'POST':
    print "helloooooo"
    if form.validate() == False:
      print form.errors
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      print "hihihihihi"
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['mitzisong@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)











