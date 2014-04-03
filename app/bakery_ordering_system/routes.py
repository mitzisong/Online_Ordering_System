from bakery_ordering_system import app, models
from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import ContactForm, SignupForm, DeliveryRecipientForm, ChooseDecorationsForm
from flask.ext.mail import Message, Mail
from models import Customer, Delivery_Recipient, Order_Product, Product, Order, session as dbsession
import datetime

mail = Mail()

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
    # print "DELIVERYMETHOD", deliveryrecipientform.deliverymethod.data
    if deliveryrecipientform.deliverymethod.data=="True":
      # print "I AM SET FOR PICK UP"
      if form.validate_on_submit():
          newuser = Customer(firstname = form.firstname.data, 
                             lastname  = form.lastname.data, 
                             phonenumber = form.phonenumber.data, 
                             email = form.email.data)
          dbsession.add(newuser)
          dbsession.commit()
          newuser_id = models.session.query(Customer).order_by(Customer.id.desc()).first()


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
    deliveryrecipient_id = models.session.query(Delivery_Recipient).order_by(Delivery_Recipient.id.desc()).first()
    print "DELIVERY RECIPIENT ID", deliveryrecipient_id.id
    # print "This is the time", form.time.data
    # print "This is the day", form.day.data
    # print "This is the month", form.month.data
    # print "This is the year", form.year.data
    date_string = form.month.data + "-" + form.day.data + "-" + form.year.data
    my_date = datetime.datetime.strptime(date_string, "%b-%d-%Y")
    time_string = form.time.data
    date_time_string = date_string + " " + time_string
    my_date_time = datetime.datetime.strptime(date_time_string, "%b-%d-%Y %H:%M")
    # print my_date_time
    # print "DELIVERYMETHOD", deliveryrecipientform.deliverymethod.data
    # newuser_id = models.session.query(Customer)
    neworder = Order(customer_id = newuser_id.id,
                     recipients_id = deliveryrecipient_id.id,
                     date_time = my_date_time,
                     delivery = deliveryrecipientform.deliverymethod.data)

    dbsession.add(neworder)
    dbsession.commit()

    return redirect(url_for('order2'))
    # , order_id=neworder.id


  return render_template('order.html', form=form,
                                       deliveryrecipientform=deliveryrecipientform)

@app.route('/order2', methods = ['GET', 'POST'])
def order2():
  minis = models.session.query(Product).filter_by(size="mini")
  regulars = models.session.query(Product).filter_by(size="regular")


  if request.method == "POST":
    neworder_id = models.session.query(Order).order_by(Order.id.desc()).first()
    whole_form = request.form
    for product_id in whole_form.iterkeys():
      if whole_form[product_id] != "":
        print "These cupcakes:", product_id, whole_form[product_id]
  
        new_order_product = Order_Product(order_id = neworder_id.id,
                                          product_id = int(product_id),
                                          quantity = int(whole_form[product_id]))
        dbsession.add(new_order_product)
        dbsession.commit()

    return redirect(url_for('order3'))

  return render_template('order2.html', minis_products = minis,
                                        reg_products = regulars)

@app.route('/order3', methods = ['GET', 'POST'])
def order3():
  choosedecorationsform = ChooseDecorationsForm(csrf_enabled=False)
  colors = choosedecorationsform.color1.data+"-"+choosedecorationsform.color2.data+"-"+choosedecorationsform.color3.data

  if request.method=="POST":
    print choosedecorationsform.color1.data
    print "THESE ARE THE COLORS", colors 
    print choosedecorationsform.decoration.data
    neworder = models.session.query(Order).order_by(Order.id.desc()).first()
    neworder.decorationtheme = choosedecorationsform.decoration.data
    neworder.colorscheme = colors

    dbsession.commit()

    return redirect(url_for('confirmation'))

  return render_template('order3.html', choosedecorationsform=choosedecorationsform)

@app.route('/confirmation')
def confirmation():

  return render_template('confirmation.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm(request.form)
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
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











