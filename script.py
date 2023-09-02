from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/nav')
def nav():
	return render_template('nav.html')

@app.route('/<string:url>')
def sign_in(url):
	return render_template(f'{url}.html')

if __name__ == '__main__':
		app.run(debug=True)