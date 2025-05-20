from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import Optional, Email, IPAddress, MacAddress, URL, InputRequired

class DeviceForm(FlaskForm):
    ip_address = StringField('IP Address', validators=[IPAddress()])
    name = StringField('Name', validators=[InputRequired()])
    mac_address = StringField('MAC Address', validators=[MacAddress(), Optional()])
    owner_id = SelectField('Owner', coerce=int)
    sub_owner_id = SelectField('Sub-Owner', coerce=int)
    serial_number = StringField('Serial Number', validators=[Optional()])
    location_id = SelectField('Location', coerce=int)
    vlan = StringField('VLAN', validators=[Optional()])
    pvlan = StringField('PVLAN', validators=[Optional()])
    os = StringField('Operating System', validators=[InputRequired()])
    is_labelled = BooleanField('Is Labelled')
    has_local_admin = BooleanField('Has Local Admin')
    wall_port = StringField('Wall Port', validators=[Optional()])
    switch = StringField('Switch', validators=[Optional()])
    switch_port = StringField('Switch Port', validators=[Optional()])
    tool_id = SelectField('Tool', coerce=int)
    is_backed_up = BooleanField('Is Backed Up')
    asset_portfolio = StringField('Asset Portfolio', validators=[URL(), Optional()])

class OwnerForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('e-mail', validators=[Email()])
    wwid = StringField('WWID', validators=[Optional()])

class LocationForm(FlaskForm):
    name = StringField('Location name', validators=[InputRequired()])
    building = StringField('Building', validators=[InputRequired()])
    lab_group = StringField('Lab Group', validators=[InputRequired()])