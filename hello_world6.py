from flask import Flask
from flask import request
from flask import render_template

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


@app.route('/mf')
def mfwebsite():
	return render_template('Motherfucking Website.html')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500


@app.route('/testePost', methods=['POST'])
def testePost():
	jsonData = request.get_json()
	return jsonData["senha"]


@app.route('/testeGet', methods=['GET'])
def testeGet():
	return "GET!", 200


@app.route('/testeGetPost', methods=['POST', 'GET'])
def testeGetPost():
	if request.method == 'POST':
		jsonData = request.get_json()
		return jsonData["senha"]
	else:
		return "GET!", 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
