
from flask import Blueprint, session, render_template, request, redirect, url_for, flash

#from . import api_rooms
#from ._utils import call


blueprint = Blueprint('test', __name__)


@blueprint.route("/test")
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@blueprint.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        if request.form['username'] is not None and request.form['username']!='':
            session['username'] = request.form['username']
            return "Thank you for logging in {0} <br></br> <a href='/logout'>Logout</a>".format(session['username'])
        else:
            return "Please provide a valid value for the username: " + render_template("login.html")
    return render_template("login.html")

@blueprint.route('/logout')
def logout():
    # remove the username from the session if it's there
    username = session.pop('username', None)
    if (username is not None):
         return "Session ended.  See you later {0}! ".format(username)
    else:
        return "Session Ended."


