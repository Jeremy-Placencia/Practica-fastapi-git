import mysql.connector
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

def get_user_by_id(user_id: int):
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()

    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    return user

def get_all_users():
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return users

def create_user(nombre: str, edad: int):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO users (Nombre, Edad) VALUES (%s, %s)", (nombre, edad))
    conexion.commit()
    cursor.close()

def eliminar_user(id: int):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()