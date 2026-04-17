# Practica FastAPI + MySQL

REST API construida con FastAPI y MySQL. Permite gestionar usuarios con operaciones CRUD completas.

## Tecnologías

- Python 3.x
- FastAPI
- MySQL
- mysql-connector-python

## Instalación

1. Clona el repositorio
```bash
   git clone https://github.com/Jeremy-Placencia/Practica-fastapi-git.git
   cd Practica-fastapi-git
```

2. Instala las dependencias
```bash
   pip install fastapi uvicorn mysql-connector-python python-dotenv
```

3. Crea un archivo `.env` en la raíz con tus credenciales
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=backend

4. Corre el servidor
```bash
   uvicorn main:app --reload
```

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /users | Obtener todos los usuarios |
| GET | /users/{id} | Obtener un usuario por ID |
| POST | /users | Crear un usuario |
| DELETE | /users/{id} | Eliminar un usuario |