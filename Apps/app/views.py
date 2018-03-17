from flask import Flask, render_template, flash   
from Apps.app import apps #import flask instance
from Apps.app.form import LoginForm #class LoginForm inheriting from Flaskforms
from Apps.app.signupform import SignupForm
# for the index page
@apps.route('/', methods=['GET','POST' ])
@apps.route('/index', methods=['GET','POST'])
def index ():
	form =LoginForm()
	# if form.validate_on_submit():
	# 	flash("error message",category='error' )
	return render_template("index.html",
						    form=form
					)

#for the signup form
@apps.route('/signup',methods=['GET','POST'])
def signup ():
	forms=SignupForm()
	return render_template ("signup.html",
							form=forms
	                 )

@apps.route('/home', methods=['GET','POST'])
def home():
	return render_template("home.html")
