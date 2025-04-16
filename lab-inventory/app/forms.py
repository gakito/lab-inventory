from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Optional

class DeviceForm(FlaskForm):
    ip_address = StringField('IP Address', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[DataRequired()])
    owner_id = SelectField('Owner', coerce=int)
    sub_owner_id = SelectField('Sub-Owner', coerce=int, validators=[Optional()])
    serial_number = StringField('Serial Number', validators=[DataRequired()])
    location_id = SelectField('Location', coerce=int)
    vlan = StringField('VLAN', validators=[DataRequired()])
    pvlan = StringField('PVLAN', validators=[DataRequired()])
    os = StringField('Operating System', validators=[DataRequired()])
    is_labelled = BooleanField('Is Labelled')
    has_local_admin = BooleanField('Has Local Admin')
    wall_port = StringField('Wall Port', validators=[DataRequired()])
    switch = StringField('Switch', validators=[DataRequired()])
    switch_port = StringField('Switch Port', validators=[DataRequired()])
    tool_id = SelectField('Tool', coerce=int)
    is_backed_up = BooleanField('Is Backed Up')