from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

blueprint = Blueprint('index', __name__)


@blueprint.route("/")
@login_required
def index():
    return render_template("index.html")

@login_required
@blueprint.route("/participant_search/")
def participant_search():
    return render_template("index.html")

@login_required
@blueprint.route("/dispense_order/")
def dispense_order():
    return render_template("dispenseorder.html")

@login_required
@blueprint.route("/reversal_report/")
def reversal_report():
    return render_template("reversalreport.html")
