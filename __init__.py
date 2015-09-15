from flask import Flask
app = Flask(__name__)

emails = {"aputman@hmc.edu": {'name': 'Alex Putman', 'age': 21}}

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/api/<email>')
def api(email):
	if (email in emails):
		return flask.jsonify(**emails[email])
	else:
		abort(404)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
