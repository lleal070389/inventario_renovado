from webapp.models import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)

    people = db.relationship("People", back_populates="users", lazy=True)
    customer = db.relationship("Customer", back_populates="users", lazy=True)

    @classmethod
    def all(self):
        return User.query.all()

    def to_json(self):
        response = {
            "id": self.id
        } | {"person": self.people.to_json()} | {"customer": self.customer.to_json()}
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