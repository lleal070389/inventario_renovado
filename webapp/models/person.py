from webapp.models import db

from babel.dates import format_datetime
from datetime import datetime


class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Integer, nullable=False, default=0)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.today())
    update_time = db.Column(db.DateTime, nullable=True)

    users = db.relationship("User", back_populates="people", lazy=True)

    @classmethod
    def all(self):
        return Person.query.all()

    def to_json(self):
        response = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": True if self.is_admin else False
        }
        return response

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def _create_time(self, locale="es_CL"):
        return format_datetime(self.create_time, locale=locale) if self.create_time else ""

    def _update_time(self, locale="es_CL"):
        return format_datetime(self.update_time, locale=locale) if self.update_time else ""
