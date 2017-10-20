from flask import render_template,session,redirect, url_for
from flask_login import login_required
from . import main
from .. import db
from ..models import User


@main.route('/',methods=['POST','GET'])
@login_required
def index():
    return 'ok',200


