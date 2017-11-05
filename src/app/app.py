import logging

from flask import Response, redirect
from flask_api import FlaskAPI
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_admin.contrib.sqla import ModelView
from .models import AdminUserModel, ClientUserModel, ParticipantInfoModel, LocationModel, DrugsModel, ReversalDrugsModel, OverdoseReversalsModel, SyringeModel, SyringeAccessModel, SyringeAccessSyringesModel, CountyModel, PreventionModel, OverdoseResponseModel, OrderDispenseModel, OrderDispenseDrugsModel, OrderDispensePreventionModel, OrderDispenseOverdoseResponseModel
from werkzeug.exceptions import HTTPException


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


from . import views
from . import extensions


log = logging.getLogger(__name__)


def create_app(config):
    app = FlaskAPI(__name__)
    app.config.from_object(config)
    app.config['BASIC_AUTH_USERNAME'] = 'admin'
    app.config['BASIC_AUTH_PASSWORD'] = 'admin'
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)

    from flask_admin.contrib.sqla import ModelView

    class ModelView(ModelView):

        column_display_pk = True
        column_display_all_relations = True

        @property
        def is_accessible(self):
            if not basic_auth.authenticate():
                raise AuthException('Not authenticated.')
            else:
                return True

        @property
        def inaccessible_callback(self, name, **kwargs):
            return redirect(basic_auth.challenge())



    configure_logging(app)

    register_blueprints(app)
    register_extensions(app)

    return app


def configure_logging(app):
    if app.config['DEBUG']:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def register_blueprints(app):
    register_backend(app)
    register_frontend(app)


def register_backend(app):
    app.register_blueprint(views.api_root.blueprint)
    app.register_blueprint(views.api_participant.blueprint)


def register_frontend(app):
    app.register_blueprint(views.index.blueprint)


def register_extensions(app):
    extensions.db.init_app(app)
    admin = Admin(app, name='Admin Console', template_mode='bootstrap3')
    admin.add_view(ModelView(ClientUserModel, extensions.db.session))
    admin.add_view(ModelView(ParticipantInfoModel, extensions.db.session))
    admin.add_view(ModelView(LocationModel, extensions.db.session))
    admin.add_view(ModelView(DrugsModel, extensions.db.session))
    admin.add_view(ModelView(OverdoseReversalsModel, extensions.db.session))
    admin.add_view(ModelView(SyringeModel, extensions.db.session))
    admin.add_view(ModelView(SyringeAccessModel, extensions.db.session))
    admin.add_view(ModelView(CountyModel, extensions.db.session))
    admin.add_view(ModelView(PreventionModel, extensions.db.session))
    admin.add_view(ModelView(OverdoseResponseModel, extensions.db.session))
    admin.add_view(ModelView(OrderDispenseModel, extensions.db.session))
