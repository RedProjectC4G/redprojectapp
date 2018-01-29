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
    if form.is_submitted():
        if form.find_by_code.data:
            print('in find_by_code')
            """check for participant code in db"""
            participant = Participant.objects(participant_code=form.participant_code.data).first()
            print(participant)
            if participant:
                return redirect(url_for('index.existing_client',participant_code=form.participant_code.data))
            else:
                error = 'Invalid Participant'
        else:
            print('in find_by_parts')
            print(form.validate())
            """check for participant by parts and goto next step if doesn't exist"""
            participant_code = (form.gender.data + form.first_name_initial.data + '{:02d}{:02d}'.format(int(form.birthday_month.data), int(form.birthday_year.data)) + form.mother_first_name_initial.data).upper()
            print(participant_code)
            participant = Participant.objects(participant_code=participant_code).first()
            print(participant)
            if not participant:
                Participant(participant_code = participant_code).save()

            return redirect(url_for('index.existing_client',participant_code=participant_code))
    return render_template("index.html",form=form,error=error)

@blueprint.route("/existing_client/",methods=['GET','POST'])
@login_required
def existing_client():
    participant_code = request.args.get('participant_code')
    participant = Participant.objects(participant_code=participant_code).first()
    print(participant.birthdate)
    return render_template("existingclient.html", participant=participant)

@login_required
@blueprint.route("/dispense_order/")
def dispense_order():
    return render_template("dispenseorder.html")

@login_required
@blueprint.route("/reversal_report/")
def reversal_report():
    return render_template("reversalreport.html")
