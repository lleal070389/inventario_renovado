from flask import Blueprint

from webapp.models.customer import Customer
from webapp.models.item import Item
from webapp.models.state import State
from webapp.models.user import User

from webapp.responses import response

api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_v1.get("/customers")
def get_customers():
    customers = [customer.to_json() for customer in Customer.all()]
    return response(customers=customers)


@api_v1.get("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    return response(customer=customer.to_json())


@api_v1.get("/items")
def get_items():
    items = [item.to_json() for item in Item.all()]
    return response(items=items)


@api_v1.get("/items/<int:item_id>")
def get_item(item_id):
    item = Item.query.get(item_id)
    return response(item=item.to_json())


@api_v1.get("/states")
def get_states():
    states = [state.to_json() for state in State.all()]
    return response(states=states)


@api_v1.get("/states/<int:state_id>")
def get_state(state_id):
    state = State.query.get(state_id)
    return response(state=state.to_json())


@api_v1.get("/users")
def get_users():
    users = [user.to_json() for user in User.all()]
    return response(users=users)


@api_v1.get("/users/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    return response(user=user.to_json())
