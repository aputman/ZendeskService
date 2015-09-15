from flask import Flask
from flask import jsonify
app = Flask(__name__)

emails = {'aputman@hmc.edu': {'name': 'Alex Putman', 'age': 21}, '': {'win': True}}

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/api/<email>')
def api(email):
	return email
	#if (email in emails):
	#	return email
	#else:
	#	abort(404)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
