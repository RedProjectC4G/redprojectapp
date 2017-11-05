from flask import Blueprint, render_template, request, redirect, url_for, flash

#from . import api_rooms
#from ._utils import call


blueprint = Blueprint('index', __name__)


@blueprint.route("/")
def get():
    return render_template("index.html")
