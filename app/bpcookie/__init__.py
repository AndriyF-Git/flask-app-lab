from flask import Blueprint
import click

cook_bp = Blueprint("cook", __name__, url_prefix="/process")

from . import views
