from flask import Blueprint, render_template, redirect, url_for, request
from .models import Device, db
from .forms import DeviceForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    devices = Device.query.all()
    return render_template('index.html', devices=devices)

@bp.route('/device/add', methods=['GET', 'POST'])
def add_device():
    form = DeviceForm()
    if form.validate_on_submit():
        device = Device(
            ip_address=form.ip_address.data,
            name=form.name.data,
            mac_address=form.mac_address.data,
            owner_id=form.owner_id.data,
            sub_owner_id=form.sub_owner_id.data,
            serial_number=form.serial_number.data,
            location_id=form.location_id.data,
            vlan=form.vlan.data,
            pvlan=form.pvlan.data,
            os=form.os.data,
            is_labelled=form.is_labelled.data,
            has_local_admin=form.has_local_admin.data,
            wall_port=form.wall_port.data,
            switch=form.switch.data,
            switch_port=form.switch_port.data,
            tool_id=form.tool_id.data,
            is_backed_up=form.is_backed_up.data
        )
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('device/create.html', form=form)