from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..forms import ParticipantForm
from ..models import Participant

blueprint = Blueprint('index', __name__)



@blueprint.route("/",methods=['GET','POST'])
@blueprint.route("/participant_search/",methods=['GET','POST'])
@login_required
def index():
    error = None
    form=ParticipantForm(request.form)
    print(form.data)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('post val')
        if form.find_by_code.data:
            """check for participant code in db"""
            participant = Participant.objects(participant_code=form.participant_code.data).first()
            print(participant)
            if participant:
                return redirect(url_for('index.existing_client',participant_code=form.participant_code.data))
            else:
                error = 'Invalid Participant'
        else:
            """check for participant by parts and goto next step if doesn't exist"""
        print(error)
    return render_template("index.html",form=form,error=error)

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
