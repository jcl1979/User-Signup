from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template("inputs.html")

@app.route("/form_valid", methods=["POST"])
def valid_user_signup():
    user_name = request.form["user_name"]
    name_error = ''
    if len(user_name) > 20 or len(user_name) < 3 or user_name == '':
        name_error ="That's not a valid username"


    password = request.form["password"] 
    pass_error = ''
    if len(password) > 20 or len(password) < 3 or password == '':
        pass_error ="That's not a valid password"


    
    confirm_password = request.form["confirm_password"]
    confirm_error = ''
    if password != confirm_password or confirm_password == '':
        confirm_error = " Passwords don't match"


    email = request.form["email"]
    first_test = email.split("@")
    second_test = email.split(".")
    third_test = email.count(" ")
    email_error =''

    if len(email) >= 1:
        if len(email) > 20 or len(email) < 3:
            email_error = "That's not a valid email" 
        if len(first_test) != 2 or len(second_test) != 2 or third_test != 0:
            email_error = "That's not a valid email" 


    if not name_error and not pass_error and not confirm_error and not email_error:
        return render_template("welcome.html", user_name=user_name)
    else:
        return render_template("inputs.html", name_error=name_error, pass_error=pass_error,
            confirm_error=confirm_error, email_error=email_error, user_name=user_name)    
        
        

app.run()