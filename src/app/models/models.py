
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
    """ Holds the 8 digit code for users that are using the client """
    __tablename__ = 'client_users'

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String)

class ParticipantInfoModel(BaseModel):
    """ Holds the data from the client intake form """
    __tablename__ = 'participant_info'

    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey("client_users.id"), nullable=False)
    intake_data = db.Column(db.JSON)

class LocationModel(BaseModel):
    """ Holds the information regarding the available locations that participants can visit """
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

class DrugsModel(BaseModel):
    """ Holds information about which drugs are available to select """
    __tablename__ = 'drugs'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    category = db.Column(db.String)

class ReversalDrugsModel(BaseModel):
    """ Join table linking a record in the overdose_reversals table to records in the drugs table """
    __tablename__ = 'overdose_reversal_drugs'

    id = db.Column(db.Integer, primary_key = True)
    reversal_id = db.Column(db.Integer, db.ForeignKey("overdose_reversals.id"), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey("drugs.id"), nullable=False)

class OverdoseReversalsModel(BaseModel):
    """ Holds information about overdose reversals, supplies used, and steps performed """
    __tablename__ = 'overdose_reversals'

    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey("client_users.id"), nullable=False)
    date = db.Column(db.Date)
    county = db.Column(db.String)
    site = db.Column(db.String)
    date_of_overdose = db.Column(db.Date)
    time_before_naloxone = db.Column(db.Integer)
    naloxone_amount = db.Column(db.Integer)
    num_intra_nasal_doses = db.Column(db.Integer)
    route = db.Column(db.String)
    performed_rescue_breathing = db.Column(db.Boolean)
    used_barrier = db.Column(db.Boolean)
    overdose_returned_time = db.Column(db.Integer)
    police_called = db.Column(db.Boolean)
    employee_initials = db.Column(db.String)

class SyringeModel(BaseModel):
    """ Holds information about the different syringe models """
    __tablename__ = 'syringes'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

class SyringeAccessModel(BaseModel):
    """ Holds information from the syringe access form """
    __tablename__ = 'syringe_access'

    id = db.Column(db.Integer, primary_key = True)
    new_client = db.Column(db.Boolean)
    safe_crack_supplies = db.Column(db.Boolean)
    num_overdose_kits = db.Column(db.Integer)
    seconday_syringe_exchange = db.Column(db.Integer)

class SyringeAccessSyringesModel(BaseModel):
    """ Join table between the syringe_access table and the syringes table """
    __tablename__ = 'syringe_access_syringes'

    id = db.Column(db.Integer, primary_key = True)
    syringe_access_id = db.Column(db.Integer, db.ForeignKey("syringe_access.id"), nullable=False)
    syringe_id = db.Column(db.Integer, db.ForeignKey("syringes.id"), nullable=False)
    count = db.Column(db.Integer)
