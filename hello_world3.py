from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
	return '<h1>Hello World!</h1>'


@app.route('/userAgent')
def userAgent():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
