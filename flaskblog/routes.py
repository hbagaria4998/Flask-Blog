from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegistraionForm,LoginForm
from flaskblog.models import User,Post
from flaskblog import app


posts = [
	{
	'author': 'himanshu Bagaria',
	'title': 'Blog post 1',
	'content': "content 1",
	'date_posted': 'April 20, 2018'
	},
	{
	'author': 'himanshu Bagaria',
	'title': 'Blog post 1',
	'content': "content 1",
	'date_posted': 'April 20, 2018'
	}

]

@app.route("/")
def home():
	return render_template('home.html',posts = posts)

@app.route("/about")
def about():
	return render_template('about.html',title = 'About')

@app.route("/register",methods = ['GET','POST'])
def register():
	form = RegistraionForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html',title = 'Register',form = form)

@app.route("/login",methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful','danger')
	return render_template('login.html',title = 'Login',form = form)
