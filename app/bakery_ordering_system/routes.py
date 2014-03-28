from bakery_ordering_system import app
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm, SignupForm, DeliveryRecipientForm
from flask.ext.mail import Message, Mail
from models import Customer, Delivery_Recipient, session as dbsession

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

@app.route('/order', methods=['GET', 'POST'])
def order():
  form = SignupForm(csrf_enabled=False)
  deliveryrecipientform = DeliveryRecipientForm(csrf_enabled=False)

  if request.form.get("deliverymethod")=="pickup":
    if form.validate_on_submit():
        newuser = Customer(firstname = form.firstname.data, 
                           lastname  = form.lastname.data, 
                           phonenumber = form.phonenumber.data, 
                           email = form.email.data)
        dbsession.add(newuser)
        dbsession.commit()

        return redirect(url_for('order2'))

  elif request.form.get("deliverymethod")=="delivery":
    if deliveryrecipientform.validate_on_submit():
        deliveryrecipient = Delivery_Recipient(name = deliveryrecipientform.name.data,
                                               phonenumber = deliveryrecipientform.phonenumber.data,
                                               companyname = deliveryrecipientform.companyname.data,
                                               streetaddress = deliveryrecipientform.streetaddress.data,
                                               unit = deliveryrecipientform.unit.data,
                                               city = deliveryrecipientform.city.data,
                                               state = deliveryrecipientform.state.data,
                                               zipcode = deliveryrecipientform.zipcode.data)
        dbsession.add(deliveryrecipient)
        dbsession.commit()

        return redirect(url_for('order2'))


  return render_template('order.html', form=form,
                                       deliveryrecipientform=deliveryrecipientform)
  print "hello"

@app.route('/order2')
def order2():
  choosecupcakesform = ChooseCupcakesForm(csrf_enabled=False)

  return render_template('order2.html', choosecupcakesform=choosecupcakesform)

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


































