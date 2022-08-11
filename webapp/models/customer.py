from webapp.models import db

from babel.dates import format_datetime
from datetime import datetime


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    token = db.Column(db.String(45), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.today())
    update_time = db.Column(db.DateTime, nullable=True)

    users = db.relationship("User", back_populates="customer", lazy=True)
    items = db.relationship("Item", back_populates="customer", lazy=True)

    @classmethod
    def all(self):
        return Customer.query.all()

    def to_json(self, locale="es_CL"):
        response = {
            "id": self.id,
            "name": self.name,
            "create_time": format_datetime(self.create_time, locale=locale),
            "update_time": format_datetime(self.update_time, locale=locale)
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
