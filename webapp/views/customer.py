from flask import Blueprint
from flask import render_template
from flask import request

from webapp.models import db
from webapp.models.customer import Customer

from uuid import uuid4
from datetime import datetime


customers = Blueprint("customers", __name__, url_prefix="/customers")


@customers.get("/")
def customers_index():
    customers = Customer.all()
    return render_template("customers/index.html",
                           page={"title": "Organizaciones"},
                           customers=customers)


@customers.get("/add")
@customers.post("/add")
def customers_add():
    if request.method == "GET":
        return render_template("customers/customer.html",
                               page={"title": "Nuevo Registro"},
                               token=uuid4())

    elif request.method == "POST":
        name = request.form.get("name").strip()
        token = request.form.get("token").strip()

        if Customer.query.filter_by(name=name).all():
            return {"status": "warning", "message": "Nombre duplicado"}
        if Customer.query.filter_by(token=token).all():
            return {"status": "warning", "message": "Token duplicado"}

        customer = Customer(name=name, token=token)
        if customer.save():
            return {"status": "success", "message": "Nuevo registro exitoso"}
        return {"status": "danger", "message": "Registro no ingresado"}


@customers.get("/edit/<int:customer_id>")
@customers.post("/edit/<int:customer_id>")
def customers_edit(customer_id):
    customer = Customer.query.get(customer_id)

    if request.method == "GET":
        return render_template("customers/customer.html",
                               page={"title": f"Editar {customer.name}"},
                               customer=customer,
                               token=uuid4())

    elif request.method == "POST":
        name = request.form.get("name").strip()
        token = request.form.get("token").strip()

        if customer.name != name and Customer.query.filter_by(name=name).first():
            return {"status": "warning", "message": "Nombre duplicado"}

        if customer.token != token and Customer.query.filter_by(token=token).first():
            return {"status": "warning", "message": "Token duplicado"}

        if customer.name == name and customer.token == token:
            return {"status": "info", "message": "Registro sin cambios"}

        customer.name = name
        customer.token = token
        customer.update_time = datetime.today()
        db.session.commit()
        return {"status": "success", "message": "Registro editado"}


@customers.delete("/delete/<int:customer_id>")
def customers_delete(customer_id):
    customer = Customer.query.get(customer_id)
    if customer.delete():
        return {"status": "success", "message": "Registro eliminado"}
    return {"status": "danger", "message": "No se pudo eliminar"}