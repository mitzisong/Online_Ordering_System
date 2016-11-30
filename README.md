ONLINE ORDERING SYSTEM for Mitzi's Cupcakes
======================
An Online Ordering System created for my pseudo bakery - Mitzi's Cupcakes.

Overview
========
My inspiration to create an online ordering system came from previously being a Wedding & Events Manager at a bakery and witnessing how much real world application an online ordering system would have to the bakery's ordering process. If the option is available, most customers would prefer placing an order through an online ordering system rather than holding a frustrating conversation over the phone - or even a back-and-forth email dance. Mitzi's Cupcakes' Online Ordering System utilizes Python, Flask, WTForms, SQLAlchemy, PostgreSQL, Jinja, HTML, CSS, Javascript, jQuery, ToolTip.

![screenshot1](https://raw.githubusercontent.com/mitzisong/Online_Ordering_System/master/app/bakery_ordering_system/static/img/Screenshot1.png)

Back-End
========
The web framework for my application is built using Flask. 

When it came to seeding and populating my database tables, I used PostgreSQL and SQLAlchemy. Every time seed.py is called, it utilizes SQLAlchemy to recreate a PostgreSQL database and insert the data into the Products data table. SQLAlchemy maps the classes written in Python with my database tables. The remaining database tables are populated when the user fills out the forms on the browser.

I used WTForms, which is a library designed to make the process of form data submitted by a browser easier to handle. WTForms is utitlized in my Contact page as well as the primary page of my Online Ordering System.

![screenshot1](https://raw.githubusercontent.com/mitzisong/Online_Ordering_System/master/app/bakery_ordering_system/static/img/Screenshot5.png)

Front-end Magic
===============
Styling my web-application was an enjoyable task for me. The screenshot below displays the hover-over text I was able to accomplish using ToolTip - it's the little things!

![screenshot1](https://raw.githubusercontent.com/mitzisong/Online_Ordering_System/master/app/bakery_ordering_system/static/img/Screenshot14.png)

As a visual person, being able to see all the code come alive on the web browser is very satisfying for me. Using jQuery to hide and show features almost seems like performing a magic trick! 

Final Thoughts
==============
Through this project I was able to deepen my understanding on how the front-end and back-end communicate with each other in web applications and gain a better grasp on how the full stack functions.
