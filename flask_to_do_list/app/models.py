from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(100),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="pending"
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    user = db.relationship(
        "Users",
        back_populates="tasks"
    )


class Users(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    tasks = db.relationship(
        "Task",
        back_populates="user",
        cascade="all, delete"
    )

    def set_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)