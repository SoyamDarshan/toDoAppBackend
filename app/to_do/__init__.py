from flask import Blueprint

bp = Blueprint('to_do', __name__)

from app.to_do import routes