from ..extensions import mongo

class Participant(mongo.DynamicDocument):
    participant_code = mongo.StringField(required=True)
    birthdate = mongo.DateTimeField()
    residence = mongo.StringField(max_length=50)
    zip_code = mongo.StringField(max_length=50)
    expense_type = mongo.StringField(max_length=50)
    dependents = mongo.IntField()
    ethnicity = mongo.StringField(max_length=50)
    income = mongo.IntField()
    mothers_initial = mongo.StringField(max_length=2)
