from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

blueprint = Blueprint('index', __name__)


@blueprint.route("/")
@login_required
def get():
    return render_template("index.html")

@blueprint.route("/participant_search")
def participant_search():
    return render_template("participants_existing.html")
