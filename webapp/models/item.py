from webapp.models import db


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.JSON, nullable=False)
    output = db.Column(db.JSON, nullable=True)
    task_id = db.Column(db.String(45), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    update_time = db.Column(db.DateTime, nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)

    state = db.relationship("State", back_populates="items", lazy=True)
    customer = db.relationship("Customer", back_populates="items", lazy=True)

    @classmethod
    def all(self):
        return Item.query.all()

    def to_json(self):
        response = {
            "id": self.id,
            "input": self.first_name,
            "output": self.last_name
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
