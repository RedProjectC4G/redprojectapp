import time
import logging
import sys
from flask import Blueprint, request, url_for
from flask_api import status

#from ..models import StubModel

blueprint = Blueprint('api_participant', __name__, url_prefix="/api/participant")
log = logging.getLogger(__name__)

@blueprint.route("/find", methods=['POST'])
def find_participant():
    if request.method == 'POST':
        if 'participant_code' in request.form:
            """ Validate participant code """
            return request.form['participant_code'], status.HTTP_200_OK

    return "error /find", status.HTTP_200_OK

@blueprint.route('/find_by_parts', methods=['POST'])
def find_participant_by_parts():
    if request.method == 'POST':
        return "find_by_parts", status.HTTP_200_OK
    return "error", status.HTTP_200_OK
