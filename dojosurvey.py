from flask import Flask, render_template, request, redirect
app = Flask (__name__)

@app.route('/')
def index():
	return render_template('main.html')

@app.route('/survey' , methods = ['POST'])
def create_user():
		# name = request.form['name']
		# dojo = request.form['dojo']
		# language = request.form['language']
		# comments = request.form['comments']
		return render_template('result.html' , name = request.form['name'], dojo = request.form['dojo'], language = request.form['language'], comments = request.form['comments'])

app.run(debug=True)
