from flask import Blueprint, url_for
from flask_api import status
from ..models import ClientUser

blueprint = Blueprint('api_root', __name__)


@blueprint.route("/api")
def index():
    content = {'test': True}

    return content, status.HTTP_200_OK
