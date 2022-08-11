from flask import Blueprint
from flask import render_template
from flask import request

from webapp.models import db
from webapp.models.state import State


states = Blueprint("states", __name__, url_prefix="/states")


@states.get("/")
def states_index():
    states = State.all()
    return render_template("states/index.html",
                           page={"title": "Estados"},
                           states=states)


@states.get("/add")
@states.post("/add")
def states_add():
    if request.method == "GET":
        return render_template("states/state.html",
                               page={"title": "Nuevo Registro"})

    elif request.method == "POST":
        idState = request.form.get("id", type=int)
        name = request.form.get("name").strip().upper()
        description = request.form.get("description").strip()

        if State.query.get(idState):
            return {"status": "warning", "message": "ID duplicado"}

        if State.query.filter_by(name=name).all():
            return {"status": "warning", "message": "Nombre duplicado"}

        state = State(id=idState, name=name, description=description)
        if state.save():
            return {"status": "success", "message": "Nuevo registro exitoso"}
        return {"status": "danger", "message": "Registro no ingresado"}


@states.get("/edit/<int:state_id>")
@states.post("/edit/<int:state_id>")
def states_edit(state_id):
    state = State.query.get(state_id)

    if request.method == "GET":
        return render_template("states/state.html",
                               page={"title": f"Editar {state.name}"},
                               state=state)

    elif request.method == "POST":
        idState = request.form.get("id", type=int)
        name = request.form.get("name").strip().upper()
        description = request.form.get("description").strip()

        if state.id != idState and State.query.get(idState):
            return {"status": "warning", "message": "ID duplicado"}

        if state.name != name and State.query.filter_by(name=name).first():
            return {"status": "warning", "message": "Nombre duplicado"}

        if state.id == idState and state.name == name and state.description == description:
            return {"status": "info", "message": "Registro sin cambios"}

        state.id = idState
        state.name = name
        state.description = description
        db.session.commit()
        return {"status": "success", "message": "Registro editado"}


@states.delete("/delete/<int:state_id>")
def states_delete(state_id):
    state = State.query.get(state_id)
    if state.delete():
        return {"status": "success", "message": "Registro eliminado"}
    return {"status": "danger", "message": "No se pudo eliminar"}