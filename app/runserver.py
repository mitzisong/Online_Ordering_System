from bakery_ordering_system import app
port = int(os.environ.get('PORT', 5000)) 
app.run(host='0.0.0.0', debug=True, port=port)