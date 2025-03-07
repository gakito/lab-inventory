from flask import Blueprint, render_template
from .models import Device

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    devices = Device.query.all()
    return render_template('index.html', devices=devices)
