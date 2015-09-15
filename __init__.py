from flask import Flask
from flask import jsonify
app = Flask(__name__)

emails = {'maingocho94@gmail.com':
{
  "orders": {
    "doodad":20,
    "widget":50,
    "gewgaw":200,
    "total":270
  }
},

'alexandermputman@gmail.com':
{
  "orders": {
    "doodad":70,
    "widget":50,
    "gewgaw":70,
    "total":190
  }
},

'customer@example.com':
{
  "orders": {
    "doodad":0,
    "widget":40,
    "gewgaw":30,
    "total":70
  }
}}

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/api/<email>')
def api(email):
	if email in emails:
		return jsonify(**emails[email])
	else:
		abort(404)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
