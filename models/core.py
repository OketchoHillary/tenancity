from datetime import datetime

from utils import db


class Business(db.Model):
    __tablename__ = 'business'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=datetime.utcnow)
    location = db.Column(db.Text)

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


class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    location = db.Column(db.Text)
    latitude = db.Column(db.Text, nullable=True)
    longitude = db.Column(db.Text, nullable=True)

    business = db.relationship('Business',
                               backref=db.backref('properties',
                                                  lazy=True))  # Establish the relationship between Business and Branch

    def __init__(self, name, location, business):
        self.business = business
        self.name = name
        self.location = location

    def __repr__(self):
        return '<name {}>'.format(self.name)


class BusinessAdmins(db.Model):
    __tablename__ = 'business_admin'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('businesses', lazy=True))
    business = db.relationship('Business', backref=db.backref('admins', lazy=True))

    def __init__(self, user_id, business_id, ):
        self.user = user_id
        self.business = business_id

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    gender = db.Column(db.String(1))
    full_name = db.Column(db.String(1))
    joined_on = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=datetime.utcnow)
    role = db.Column(db.String(125))

    business = db.relationship('Business', backref=db.backref('staff', lazy=True))
