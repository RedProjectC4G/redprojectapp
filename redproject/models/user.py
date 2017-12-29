from ..extensions import mongo

class User(mongo.DynamicDocument):
    email = mongo.StringField(required=True)
    first_name = mongo.StringField(max_length=50)
    last_name = mongo.StringField(max_length=50)
    password = mongo.StringField(max_length=50)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    # Required for administrative interface
    def __unicode__(self):
        return self.email
