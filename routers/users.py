from fastapi import APIRouter
from pydantic import BaseModel
from services import user_service

router = APIRouter(prefix="/users", tags=["users"])

class Persona(BaseModel):
    Nombre: str
    Edad: int


@router.get("/")
def send_users_maybe(nombre: str = None):
    return user_service.mostrar_user_aveces(nombre)

@router.get("/{user_id}")
def get_user(user_id: int):
    return user_service.get_user_by_id(user_id)

@router.post("/")
def agregar_usuario(persona: Persona):
    user_service.create_user(persona.Nombre, persona.Edad)
    return {"mensaje": "Usuario agregado correctamente", "datos": persona}

@router.delete("/{id}")
def delete_user(id: int):
    user_service.eliminar_user(id)
    return {"mensaje": "Usuario eliminado correctamente", "ID": id, "Usuarios": user_service.get_all_users()}

@router.put("/{id}")
def edit_users(id: int, persona:Persona):
    user_service.editar_user(id,persona.Nombre,persona.Edad)
    return {"mensaje": "user actualizado correctamente", "Datos": persona}

