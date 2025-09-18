import string, random
from app import db, bcrypt

# Utility: Generate random verification code
def generate_randomkey(length: int = 8) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    verification_code = db.Column(db.String(8), nullable=False, default=generate_randomkey)
    is_active = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(20), default='user')

    # save
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Hash password
    def set_password(self, raw_password: str):
        self.password = bcrypt.generate_password_hash(raw_password).decode('utf-8')

    # Verify password
    def check_password(self, raw_password: str) -> bool:
        return bcrypt.check_password_hash(self.password, raw_password)

    def __repr__(self):
        return f"<User {self.email} | Active: {self.is_active} | Role: {self.role}>"

    @staticmethod
    def filter_by_email(email: str):
        return User.query.filter_by(email=email).first()
