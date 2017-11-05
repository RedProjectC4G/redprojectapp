
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


class AdminUserModel(BaseModel):
    __tablename__ = 'admin_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    @property
    def is_active(self):
        """True, as all users are active."""
        return True

    @property
    def get_id(self):
        """Return the username to satisfy Flask-Login's requirements."""
        return self.username

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


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
    time_before_naloxone = db.Column(db.String)
    naloxone_amount = db.Column(db.String)
    num_intra_nasal_doses = db.Column(db.Integer)
    administered_route = db.Column(db.String)
    performed_rescue_breathing = db.Column(db.Boolean)
    used_barrier = db.Column(db.Boolean)
    overdose_returned_time = db.Column(db.String)
    police_called = db.Column(db.Boolean)
    employee_initials = db.Column(db.String)
    other_drug = db.Column(db.String)
    zip_code = db.Column(db.String)
    notes = db.Column(db.Text)

class SyringeModel(BaseModel):
    """ Holds information about the different syringe models """
    __tablename__ = 'syringes'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

class SyringeAccessModel(BaseModel):
    """ Holds information from the syringe access form """
    __tablename__ = 'syringe_access'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    safe_crack_supplies = db.Column(db.Boolean)
    hiv_test = db.Column(db.Boolean)
    hcv_test = db.Column(db.Boolean)
    num_overdose_kits = db.Column(db.Integer)
    seconday_syringe_exchange = db.Column(db.Integer)
    referral_notes = db.Column(db.Text)
    general_notes = db.Column(db.Text)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    other_location = db.Column(db.String)
    employee_initials = db.Column(db.String)

class SyringeAccessSyringesModel(BaseModel):
    """ Join table between the syringe_access table and the syringes table """
    __tablename__ = 'syringe_access_syringes'

    id = db.Column(db.Integer, primary_key = True)
    syringe_access_id = db.Column(db.Integer, db.ForeignKey("syringe_access.id"), nullable=False)
    syringe_id = db.Column(db.Integer, db.ForeignKey("syringes.id"), nullable=False)
    count = db.Column(db.Integer)

class CountyModel(BaseModel):
    """ Contains the list of counties that contain locations """
    __tablename__ = 'counties'

    id = db.Column(db.Integer, primary_key = True)
    county = db.Column(db.String)

class PreventionModel(BaseModel):
    """ Contains the list of prevention methods """
    __tablename__ = 'overdose_preventions'

    id = db.Column(db.Integer, primary_key = True)
    method = db.Column(db.String)

class OverdoseResponseModel(BaseModel):
    """ Contains the list of overdose response methods and their category """
    __tablename__ = 'overdose_responses'

    id = db.Column(db.Integer, primary_key = True)
    response = db.Column(db.String)
    category = db.Column(db.String)

class OrderDispenseModel(BaseModel):
    """ Holds information from the Order to Dispense Form """
    __tablename__ = 'orders_to_dispense'

    id = db.Column(db.Integer, primary_key = True)
    race = db.Column(db.String)
    know_someone_at_risk = db.Column(db.Boolean)
    other_drug = db.Column(db.String)
    use_substances_twice_per_month = db.Column(db.Boolean)
    recent_abstinence_period = db.Column(db.Boolean)
    when_recent_abstinence = db.Column(db.Text)
    why_recent_abstinence = db.Column(db.Text)
    num_overdoses = db.Column(db.Integer)
    when_last_overdose = db.Column(db.Text)
    what_drug_last_overdose = db.Column(db.Text)
    num_overdoses_witnessed = db.Column(db.Integer)
    num_overdoses_witnessed_hospital = db.Column(db.Integer)
    num_overdoses_witnessed_died = db.Column(db.Integer)
    naloxone_lot_num = db.Column(db.String)
    naloxone_expiration_date = db.Column(db.Date)
    num_naloxone_dispensed = db.Column(db.Integer)
    narcan_lot_num = db.Column(db.String)
    narcan_expiration_date = db.Column(db.Date)
    num_narcan_dispensed = db.Column(db.Integer)
    prescriber = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    other_location = db.Column(db.String)
    employee_initials = db.Column(db.String)

class OrderDispenseDrugsModel(BaseModel):
    """ Join table between the orders_to_dispense table and the drugs table """
    __tablename__ = 'orders_to_dispense_drugs'

    id = db.Column(db.Integer, primary_key = True)
    orders_to_dispense_id = db.Column(db.Integer, db.ForeignKey("orders_to_dispense.id"), nullable=False)
    drugs_id = db.Column(db.Integer, db.ForeignKey("drugs.id"), nullable=False)

class OrderDispensePreventionModel(BaseModel):
    """ Join table between the orders_to_dispense table and the preventions table """
    __tablename__ = 'orders_to_dispense_preventions'

    id = db.Column(db.Integer, primary_key = True)
    orders_to_dispense_id = db.Column(db.Integer, db.ForeignKey("orders_to_dispense.id"), nullable=False)
    prevention_id = db.Column(db.Integer, db.ForeignKey("overdose_preventions.id"), nullable=False)

class OrderDispenseOverdoseResponseModel(BaseModel):
    """ Join table between the orders_to_dispense table and the overdose_responses table """
    __tablename__ = 'orders_to_dispense_overdose_responses'

    id = db.Column(db.Integer, primary_key = True)
    orders_to_dispense_id = db.Column(db.Integer, db.ForeignKey("orders_to_dispense.id"), nullable=False)
    overdose_response_id = db.Column(db.Integer, db.ForeignKey("overdose_responses.id"), nullable=False)

