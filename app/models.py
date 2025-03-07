from . import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50))
    name = db.Column(db.String(100))
    mac_address = db.Column(db.String(50))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    sub_owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=True)
    serial_number = db.Column(db.String(100))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    vlan = db.Column(db.String(50))
    pvlan = db.Column(db.String(50))
    os = db.Column(db.String(50))
    is_labelled = db.Column(db.Boolean)
    has_local_admin = db.Column(db.Boolean)
    wall_port = db.Column(db.String(50))
    switch = db.Column(db.String(50))
    switch_port = db.Column(db.String(50))
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'))
    is_backed_up = db.Column(db.Boolean)

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    wwid = db.Column(db.String(50), unique=True)
    devices = db.relationship('Device', foreign_keys=[Device.owner_id], backref='owner')
    sub_devices = db.relationship('Device', foreign_keys=[Device.sub_owner_id], backref='sub_owner')

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    devices = db.relationship('Device', backref='location')

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    devices = db.relationship('Device', backref='tool')