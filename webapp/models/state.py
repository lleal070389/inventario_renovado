from webapp.models import db


class State(db.Model):
    __tablename__ = "states"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    items = db.relationship("Item", back_populates="state", lazy=True)

    @classmethod
    def all(self):
        return State.query.all()

    def to_json(self):
        response = {
            "id": self.id,
            "name": self.name,
            "description": self.description
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