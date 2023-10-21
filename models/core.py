from datetime import datetime

from utils import db


class Business(db.Model):
    __tablename__ = 'business'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=datetime.utcnow)
    location = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=False)

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def save(self):
        """Save a user to the database.
        This includes creating a new user and editing one.
        """
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Branch(db.Model):
    __tablename__ = 'branch'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    location = db.Column(db.Text)
    latitude = db.Column(db.Text, nullable=True)
    longitude = db.Column(db.Text, nullable=True)

    business = db.relationship('Business', backref=db.backref('branches', lazy=True))

    def __init__(self, name, location, business):
        self.business = business
        self.name = name
        self.location = location

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name, ):
        self.name = name

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    business = db.relationship('Business', backref=db.backref('roles', lazy=True))

    def __init__(self, title, business_id):
        self.title = title
        self.business_id = business_id

    def __repr__(self):
        return '<Title {}>'.format(self.title)


class BusinessAdmins(db.Model):
    __tablename__ = 'business_admin'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    role = db.relationship('Roles', backref=db.backref('roles', lazy=True))
    user = db.relationship('User', backref=db.backref('businesses', lazy=True))
    business = db.relationship('Business', backref=db.backref('admins', lazy=True))

    def __init__(self, user_id, business_id, ):
        self.user = user_id
        self.business = business_id

    def __repr__(self):
        return '<BusinessAdmins(user_id={}, business_id={})>'.format(self.user_id, self.business_id)


class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
    gender = db.Column(db.String(1))
    full_name = db.Column(db.String(1))
    joined_on = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=datetime.utcnow)

    branch = db.relationship('Branch', backref=db.backref('staffs', lazy=True))

    def __init__(self, full_name, joined_on):
        self.full_name = full_name
        self.joined_on = joined_on

    def __repr__(self):
        return '<name {}>'.format(self.full_name)
