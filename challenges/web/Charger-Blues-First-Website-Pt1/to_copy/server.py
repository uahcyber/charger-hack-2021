
from flask import Flask, render_template, redirect, url_for, request, make_response
from flask_simplelogin import SimpleLogin, get_username, login_required

app = Flask(__name__, static_folder='static', static_url_path='')

my_users = {'admin': {'password': 'gobigblue1337', 'roles': ['admin']}}

def check_my_users(user):
	    """Check if user exists and its credentials.
	    Take a look at encrypt_app.py and encrypt_cli.py
	     to see how to encrypt passwords
	    """
	    user_data = my_users.get(user['username'])
	    if not user_data:
	        return False  # <--- invalid credentials
	    elif user_data.get('password') == user['password']:
	        return True  # <--- user is logged in!
	
	    return False  # <--- invalid credentials

SimpleLogin(app, login_checker=check_my_users)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('gimme_flag','False')
    return resp

@app.route('/admin_login_f0idl3vl4w')
@login_required(username=['admin'])
def admin():
    return render_template('success.html')

if __name__ == "__main__":
    app.run()