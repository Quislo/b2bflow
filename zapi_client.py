import os
import requests
from dotenv import load_dotenv


load_dotenv()


INSTANCE = os.getenv("ZAPI_INSTANCE")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


def enviar_mensagem(numero, mensagem):
    if not all([INSTANCE, TOKEN, CLIENT_TOKEN]):
        raise RuntimeError("Configuração Z-API incompleta no arquivo .env")

    url = (
        f"https://api.z-api.io/instances/"
        f"{INSTANCE}/token/{TOKEN}/send-text"
    )


    payload = {
        "phone": numero,
        "message": mensagem
    }


    headers = {
        "Client-Token": CLIENT_TOKEN
    }


    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=15
    )

    if not response.ok:
        raise RuntimeError(
            f"Z-API retornou {response.status_code}: {response.text}"
        )

    return response.json()
