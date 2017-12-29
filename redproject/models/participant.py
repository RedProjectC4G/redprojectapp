from ..extensions import mongo

class Participant(mongo.DynamicDocument):
    participant_code = mongo.StringField(required=True)
