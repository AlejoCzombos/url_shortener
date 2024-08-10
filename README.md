# URL Shortener

Este es un proyecto de acortador de URLs usando FastAPI y MongoDB.

## Índice

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Configuración del Entorno](#configuración-del-entorno)
- [Descripción de Entidades](#descripción-de-entidades)
  - [URL](#url)
- [API REST](#api-rest)
  - [Endpoints de URL](#endpoints-de-url)
    - [Get All URLs](#get-all-urls)
    - [Get URL by id or Alias](#get-url-by-id-or-alias)
    - [Redirect to URL](#redirect-url)
    - [Create a URL](#create-url)
    - [Update a URL by id](#update-url)
    - [Delete a URL by id](#delete-url)

## Descripción del Proyecto

El proyecto consiste en una aplicación de acortador de URLs desarrollada usando FastAPI y MongoDB.

## Tecnologías Utilizadas

- Backend:
  - FastAPI
  - Python
  - MongoDB

## Configuración del Entorno

1. Clona el repositorio
2. Crea un entorno virtual y actívalo
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate  # Para Windows
   ```
3. Instalar las dependencias
    ```bash
    pip install -r .\requirements.txt
    ```
4. Ejecuta la aplicación
    ```bash
    uvicorn src.main:app --reload
    ```
5. Accede a la aplicación en tu navegador web
    ```
    http://localhost:8000
    ```

## Descripción de Entidades

### URL
Descripción: Representa una URL acortada en el sistema.

Atributos:

`id`: String (ID de la URL, autogenerado)
`original_url`: String (URL original)
`short_url`: String (URL acortada)
`alias`: String (Alias único para la URL)
`description`: String (Descripción de la URL, opcional)
`created_at`: DateTime (Fecha de creación)
`expires_at`: DateTime (Fecha de expiración, opcional)
`password`: String (Contraseña que protege la URL, opcional)

## API REST

### Endpoints de URL

| Método | Endpoint           | Descripción                                  | Enlace Rápido               |
|--------|--------------------|----------------------------------------------|-----------------------------|
| GET    | `/`                | Obtiene todas las URLs.                      | [Get All URLs](#get-all-urls)|
| GET    | `/get/{id_or_alias}`| Obtiene una URL por ID o Alias.              | [Get URL by ID or Alias](#get-url-by-id-or-alias) |
| GET    | `/{id_or_alias}`    | Redirige a la URL original.                  | [Redirect to URL](#redirect-url) |
| POST   | `/`                | Crea una nueva URL.                          | [Create URL](#create-url)    |
| PUT    | `/{url_id}`        | Actualiza una URL existente.                 | [Update URL](#update-url)    |
| DELETE | `/{url_id}`        | Elimina una URL por su ID.                   | [Delete URL](#delete-url)    |

### Get All URLs
**Endpoint:** `GET /`

**Descripción:** Obtiene todas las URLs almacenadas en la base de datos.

**Respuesta:**
- `200 OK`: Lista de URLs obtenida exitosamente.

### Get URL by ID or Alias
**Endpoint:** `GET /get/{id_or_alias}`

**Descripción:** Obtiene una URL por su ID o Alias.

**Parámetros:**
- `id_or_alias`: String (ID o Alias de la URL)

**Respuesta:**
- `200 OK`: URL obtenida exitosamente.
- `404 Not Found`: URL no encontrada.

### Redirect URL
**Endpoint:** `GET /{id_or_alias}`

**Descripción:** Redirige a la URL original.

**Parámetros:**
- `id_or_alias`: String (ID o Alias de la URL)
- `password`: String (Contraseña para acceder, si aplica)

**Respuesta:**
- `302 Found`: Redirección exitosa.
- `401 Unauthorized`: Contraseña incorrecta.
- `404 Not Found`: URL no encontrada o expirada.

### Create URL
**Endpoint:** `POST /`

**Descripción:** Crea una nueva URL.

**Parámetros:**
- `url`: URL (Cuerpo de la solicitud con la información de la URL)

**Respuesta:**
- `201 Created`: URL creada exitosamente.
- `400 Bad Request`: Alias ya existe.

**Cuerpo de la solicitud**
```json
{
    "original_url": "String",
    "alias": "String",
    "description": "String",
    "expires_at": "datetime",
    "password": "String"
}
```

### Update URL
**Endpoint:** `PUT /{url_id}`

**Descripción:** Actualiza una URL existente.

**Parámetros:**
- `url_id`: String (ID o Alias de la URL a actualizar)
- `url`: URLUpdate (Cuerpo de la solicitud con la nueva información de la URL)

**Respuesta:**
- `200 OK`: URL actualizada exitosamente.
- `404 Not Found`: URL no encontrada.

**Cuerpo de la solicitud**
```json
{
    "original_url": "String",
    "alias": "String",
    "description": "String",
    "expires_at": "datetime",
    "password": "String"
}
```

### Delete URL
**Endpoint:** `DELETE /{url_id}`

**Descripción:** Elimina una URL por su ID.

**Parámetros:**
- `url_id`: String (ID o Alias de la URL)

**Respuesta:**
- `200 OK`: URL eliminada exitosamente.
- `404 Not Found`: URL no encontrada.
