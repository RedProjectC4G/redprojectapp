from ..models import Participant
from flask_mongoengine.wtf import model_form
from wtforms.fields import *
from flask_mongoengine.wtf.orm import validators
from datetime import datetime
from calendar import month_name

participant_form = model_form(Participant)

def form_days():
    return tuple((i, i) for i in range(1,32))

def form_months():
    return tuple((i,"{} - {}".format(i,month_name[i])) for i in range(1,13))

def form_years():
    return tuple((i,i) for i in range(1900, datetime.now().year + 1))


# Login form will provide a Password field (WTForm form field)
class ParticipantForm(participant_form):
    participant_code = StringField(validators = [validators.optional()])

    gender = RadioField('Gender', choices=[('male','Male'),('female','Female'),('non-binary', 'Non Binary')], validators = [validators.optional()])
    birthday_day = SelectField('Day', choices=form_days(), validators = [validators.optional()])
    birthday_month = SelectField('Month', choices=form_months(), validators = [validators.optional()])
    birthday_year = SelectField('Year', choices=form_years(), validators = [validators.optional()])
    first_name_initial = StringField('First Initial', validators = [validators.optional()])
    mother_first_name_initial = StringField('Mother First Initial', validators = [validators.optional()])
    find_by_code = SubmitField(label='Find')
    find_by_parts = SubmitField(label='Find or Create')
