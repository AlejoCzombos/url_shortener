import requests

from app.config import BASE_URL, CLIENT_ID, CLIENT_SECRET

def authenticate():
    url = f"{BASE_URL}/authentication"
    payload = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        # print("Token obtenido con éxito:", data["token"])
        return data["token"]
    except requests.exceptions.RequestException as e:
        print(f"Error en la autenticación: {e}")
        return None

def obtener_consulta_virtual(token, id_consulta):
    url = f"{BASE_URL}/consulta/{id_consulta}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la consulta virtual: {e} {e.response.text}")
        return None