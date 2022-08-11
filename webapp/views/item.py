from flask import Blueprint
from flask import render_template

from webapp.models.item import Item


items = Blueprint("items", __name__, url_prefix="/items")


@items.get("/")
def items_index():
    items = Item.all()
    return render_template("items.html",
                           page={"title": "Items"},
                           items=items)
