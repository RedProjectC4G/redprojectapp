from flask import Blueprint, render_template, redirect
#from . import api_rooms
#from ._utils import call


blueprint = Blueprint('index', __name__)

@blueprint.route("/")
def get():
    return redirect("/admin", code=302)
    # return render_template("index.html")
