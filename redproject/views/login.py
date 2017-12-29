from flask import Blueprint, render_template, request, redirect, url_for, flash

blueprint = Blueprint('login', __name__)

@blueprint.route("/login/", methods=['GET'])
def login():
    return render_template("login.html")
