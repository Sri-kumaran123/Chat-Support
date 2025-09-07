from app import db, bcrypt
import string, random

def generate_randomkey(length = 8) -> string:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    verification_code = db.Column(db.String(8), nullable=False, default=generate_randomkey)
    is_active = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(20), default='user')

    # Hash password
    def set_password(self, raw_password):
        self.password = bcrypt.generate_password_hash(raw_password).decode('utf-8')

    # Check password
    def check_password(self, raw_password) -> bool:
        return bcrypt.check_password_hash(self.password, raw_password)


    def __repr__(self):
        return f"<User {self.email} | Active: {self.is_active} | Role: {self.role}>"