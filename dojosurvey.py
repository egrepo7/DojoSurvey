from flask import Flask, render_template, request, redirect, flash
app = Flask (__name__)
app.secret_key = 'SHHHHH'

@app.route('/')
def index():
	return render_template('main.html')

@app.route('/survey' , methods = ['POST'])
def create_user():

	if len(request.form['name']) < 1:
		flash('Name cannot be empty!')
		return redirect('/')
	elif len(request.form['comments']) > 120:
		flash('Comments must be less than 120 characters')
		return redirect('/')
	else:
		flash('')
		return render_template('result.html' , name = request.form['name'], dojo = request.form['dojo'], language = request.form['language'], comments = request.form['comments'])


		# name = request.form['name']
		# dojo = request.form['dojo']
		# language = request.form['language']
		# comments = request.form['comments']
	return render_template('result.html' , name = request.form['name'], dojo = request.form['dojo'], language = request.form['language'], comments = request.form['comments'])

app.run(debug=True)
