from datetime import datetime

from flask_login import UserMixin

from utils import db

from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    last_login = db.Column(db.DateTime, index=False, nullable=True)
    email_confirmed = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)

    def __init__(self, contact, email, password):
        self.contact = contact
        self.email = email
        self.password = password
        self.password = generate_password_hash(password).decode()
        self.admin = False
        self.email_confirmed = False

    def __repr__(self):
        return f"<User {self.username}>"

    def save(self):
        """Save a user to the database.
        This includes creating a new user and editing one.
        """
        db.session.add(self)
        db.session.commit()
        db.session.rollback()

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks the password against it's hash to validates the user's password
        """
        return check_password_hash(self.password, password)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    # def get_reset_password_token(self, expires_in=600):
    #     return jwt.encode(
    #         {'reset_password': self.id, 'exp': time() + expires_in}, Config.SECRET_KEY, algorithm='HS256')
