from flask import Blueprint, render_template, request, redirect, url_for, flash

#from . import api_rooms
#from ._utils import call


blueprint = Blueprint('index', __name__)


@blueprint.route("/")
def get():
    return render_template("index.html")


#blueprint2 = Blueprint('participants_existing', __name__)


@blueprint.route("/participant_search")
def participant_search():
    return render_template("participants_existing.html")

