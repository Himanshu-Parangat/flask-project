#!/usr/bin/env python3
from flask import Flask,render_template

#flask instance
app = Flask(__name__)

# localhost:5000/
@app.route('/')
def index():
    return "Hellow from flask debug on !!"


# localhost:5000/login
@app.route('/login')
def login():
    return "Login Here!!"


# localhost:5000/nav
@app.route('/nav')
def nav():
    return render_template('index.html')


# localhost:5000/user/rikka
@app.route('/user/<user_name>')
def user_dashboard(user_name):
    return  render_template('user.html', name = user_name )
   # return "welcome back user %s!" % user_name 


#Invalid Url
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Internal server error
@app.errorhandler(500)
def special_exception_handler(error):
    return render_template('500.html'), 500









