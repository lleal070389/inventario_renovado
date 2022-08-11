from flask import Blueprint

from webapp.models.user import User

from webapp.responses import response

api_user = Blueprint("api_user", __name__, url_prefix="/api/user")


@api_user.get("/")
def get_users():
    users = [user.to_json() for user in User.all()]
    return response(users=users)


@api_user.get("/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    return response(user=user.to_json())
