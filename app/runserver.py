from bakery_ordering_system import app
# port = int(os.environ.get('PORT', 5000)) 
# app.run(host='0.0.0.0', debug=False, port=33507)
# app.run(host='0.0.0.0', port=port)
app.run(debug=True, host='0.0.0.0', port=5001)