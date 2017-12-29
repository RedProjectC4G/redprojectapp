from ..models import User
from flask_mongoengine.wtf import model_form
from wtforms.fields import *
from flask_mongoengine.wtf.orm import validators

user_form = model_form(User, exclude=['password'])

# Login form will provide a Password field (WTForm form field)
class LoginForm(user_form):
    email = StringField(validators=[validators.required()])
    password = PasswordField('Password',validators=[validators.Required()])

    def get_user(self):
        return User.objects(email=self.email.data).first()
