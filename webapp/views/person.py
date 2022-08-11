from flask import Blueprint
from flask import render_template
from flask import request

from webapp.models import db
from webapp.models.person import Person


from datetime import datetime


people = Blueprint("people", __name__, url_prefix="/people")


@people.get("/")
def people_index():
    people = Person.all()
    return render_template("people/index.html",
                           page={"title": "Personas"},
                           people=people)


@people.get("/add")
@people.post("/add")
def people_add():
    if request.method == "GET":
        return render_template("people/person.html",
                               page={"title": "Nuevo Registro"})

    elif request.method == "POST":
        first_name = request.form.get("first_name").strip().title()
        last_name = request.form.get("last_name").strip().title()
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")
        is_admin = request.form.get("is_admin")

        if Person.query.filter_by(email=email).all():
            return {"status": "warning", "message": "Email duplicado"}

        person = Person(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_admin=is_admin)
        if person.save():
            return {"status": "success", "message": "Nuevo registro exitoso"}
        return {"status": "danger", "message": "Registro no ingresado"}


@people.get("/edit/<int:person_id>")
@people.post("/edit/<int:person_id>")
def people_edit(person_id):
    person = Person.query.get(person_id)
    print("aquiiiii------")
    # debug(person.first_name, person.last_name, person.email, person.password, person.is_admin)

    if request.method == "GET":
        return render_template("people/person.html",
                               page={"title": f"Editar {person.first_name}"},
                               person=person)

    elif request.method == "POST":
        first_name = request.form.get("first_name").strip().title()
        last_name = request.form.get("last_name").strip().title()
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")
        is_admin = request.form.get("is_admin")
        print(first_name, last_name, email, password, is_admin)

        if person.email != email and Person.query.filter_by(email=email).first():
            return {"status": "warning", "message": "Email duplicado"}

        if person.first_name == first_name and person.last_name == last_name and person.email == email and person.password == password and person.is_admin == is_admin:
            return {"status": "info", "message": "Registro sin cambios"}

        person.first_name = first_name
        person.last_name = last_name
        person.email = email
        person.password = password
        person.is_admin = is_admin
        person.update_time = datetime.today()
        db.session.commit()
        return {"status": "success", "message": "Registro editado"}


@people.delete("/delete/<int:person_id>")
def people_delete(person_id):
    person = Person.query.get(person_id)
    if person.delete():
        return {"status": "success", "message": "Registro eliminado"}
    return {"status": "danger", "message": "No se pudo eliminar"}