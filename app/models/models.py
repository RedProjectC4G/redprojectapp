
from ..extensions import db
import datetime

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

class ClientUserModel(BaseModel):
    """ Holds the 8 digit code for users that are using the client and the data from the intake form """
    __tablename__ = 'client_users'

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String)
    intake_data = db.Column(db.JSON)

class LocationModel(BaseModel):
    """ Holds the information regarding the available locations that participants can visit """
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String)
    intake_data = db.Column(db.JSON)

class OverdoseExperienceModel(BaseModel):
    """ Holds the information about the overdose experience a participant has witnessed on a given data """
    __tablename__ = 'overdose_experiences'

    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey("client_users.id"), nullable=False)
    num_personal = db.Column(db.Integer)
    num_witnessed = db.Column(db.Integer)
    num_witnessed_hospital = db.Column(db.Integer)
    num_witnessed_dead = db.Column(db.Integer)

class DrugIntakeModel(BaseModel):
    """ Holds information about which drugs the participant has used recently to determine risk """
    __tablename__ = 'drug_intakes'

    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey("client_users.id"), nullable=False)
    date = db.Column(db.Date)
    heroin = db.Column(db.Boolean)
    methadone = db.Column(db.Boolean)
    cocain = db.Column(db.Boolean)
    alcohol = db.Column(db.Boolean)
    benzodiazapemes = db.Column(db.Boolean)
    clonodine = db.Column(db.Boolean)
    speed = db.Column(db.Boolean)
    pcp = db.Column(db.Boolean)
    other = db.Column(db.Boolean)
    unknown = db.Column(db.Boolean)

class OverdoseReversalsModel(BaseModel):
    """ Holds information about overdose reversals, supplies used, and steps performed """
    __tablename__ = 'overdose_reversals'

    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey("client_users.id"), nullable=False)
    drug_intake_id = db.Column(db.Integer, db.ForeignKey("drug_intake.id"), nullable=False)
    date = db.Column(db.Date)
    county = db.Column(db.String)
    site = db.Column(db.String)
    date_of_overdose = db.Column(db.Date)
    time_before_naloxone = db.Column(db.Integer)
    naloxone_amount = db.Column(db.Integer)
    intra_nasal_doses = db.Column(db.Integer)
    route = db.Column(db.String)
    performed_rescue_breathing = db.Column(db.Boolean)
    used_barrier = db.Column(db.Boolean)
    od_returned_time = db.Column(db.Integer)
    police_called = db.Column(db.Boolean)
    employee_initials = db.Colun(db.String)

