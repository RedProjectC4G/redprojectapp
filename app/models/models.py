from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

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
