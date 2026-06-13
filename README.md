## Stack

- Python 3.13 + Django 6 + Django REST Framework
- PostgreSQL
- Docker

**¿Por qué PostgreSQL y no MongoDB?** Los datos de empleados tienen esquema fijo, email único y no requieren flexibilidad documental.
Me parece que Mongo seria una Base mas adecuada para un catalogo de productos que pueden diferir totalmente entre sus atributos o en una situacion que requiera una base de datos distribuida con sharding

## Levantar el proyecto

Requiere Docker Desktop corriendo.

```bash
docker compose up --build
```

Esto levanta la base de datos, aplica las migraciones y arranca el servidor en `http://localhost:8000`.

## Primer uso

Crear un usuario para autenticarse:

```bash
docker compose exec web python manage.py createsuperuser
```

Obtener el token:

```
POST /api/token/
{ "username": "...", "password": "..." }
```

Usar el token en cada request:

```
Authorization: Bearer <access_token>
```

## Documentación interactiva

```
http://localhost:8000/api/docs/
```

## Tests

```bash
docker compose exec web pytest empleados/pruebas/
```

## Variables de entorno

Copiar `.env.example` como `.env` y completar los valores antes de levantar sin Docker.
