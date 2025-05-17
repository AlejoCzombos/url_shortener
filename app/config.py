import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT_EMERGENCIA_URL = os.getenv("ENDPOINT_EMERGENCIA_URL")
ENDPOINT_DESPACHO_URL = os.getenv("ENDPOINT_DESPACHO_URL")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")


if API_SECRET_KEY == "" or not API_SECRET_KEY:
    raise ValueError("API_SECRET_KEY no puede ser vacío")
if ENDPOINT_EMERGENCIA_URL == "" or not ENDPOINT_EMERGENCIA_URL:
    raise ValueError("ENDPOINT_EMERGENCIA_URL no puede ser vacío")
if ENDPOINT_DESPACHO_URL == "" or not ENDPOINT_DESPACHO_URL:
    raise ValueError("ENDPOINT_DESPACHO_URL no puede ser vacío")