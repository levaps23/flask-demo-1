from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index')
def index():
	headline = 'Once more hello word'
	return render_template('index.html', headline=)

if __name__ == '__main__':
 	app.run(port=33507)
