from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user
from ..extensions import login_manager
from ..models import User
from ..forms import LoginForm
blueprint = Blueprint('login', __name__)

@blueprint.route("/login/", methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    user = form.get_user()
    if request.method == 'POST' and form.validate():
        login_user(user)
        next = request.args.get('next')
        print(current_user)
        return redirect(next or url_for('index')) #FIXME don't let it redirect anywhere outside the site
    return render_template("login.html", form=form)

@blueprint.route("/logout/", methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('index.index'))

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()
