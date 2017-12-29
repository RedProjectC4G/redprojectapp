from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..forms import ParticipantForm

blueprint = Blueprint('index', __name__)



@blueprint.route("/",methods=['GET','POST'])
@blueprint.route("/participant_search/",methods=['GET','POST'])
@login_required
def index():
    form=ParticipantForm(request.form)
    if form.validate_on_submit():
        if form.find_by_code.data:
            """check for participant code in db"""
            print(url_for('index.existing_client',participant_code=form.participant_code.data))
            return redirect(url_for('index.existing_client',participant_code=form.participant_code.data))
        else:
            """check for participant by parts and goto next step if doesn't exist"""
    return render_template("index.html",form=form)

@blueprint.route("/existing_client/",methods=['GET','POST'])
@login_required
def existing_client():
    return render_template("existingclient.html")

@login_required
@blueprint.route("/dispense_order/")
def dispense_order():
    return render_template("dispenseorder.html")

@login_required
@blueprint.route("/reversal_report/")
def reversal_report():
    return render_template("reversalreport.html")
