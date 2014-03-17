from bakery_ordering_system import app
from flask import Flask, render_template, request, flash
from forms import ContactForm, SignupForm
from flask.ext.mail import Message, Mail
from models import Customer, session as dbsession

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
  form = SignupForm(request.form)

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('order.html', form=form)
    else:
      newuser = Customer(firstname = form.firstname.data, 
                         lastname  = form.lastname.data, 
                         phonenumber = form.phonenumber.data, 
                         email = form.email.data)
      dbsession.add(newuser)
      dbsession.commit()

      return render_template()

  elif request.method == 'GET':
    return render_template('order.html', form=form)

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


































