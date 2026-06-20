import os
import requests
from dotenv import load_dotenv


load_dotenv()


INSTANCE = os.getenv("ZAPI_INSTANCE")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


def enviar_mensagem(numero, mensagem):

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
        headers=headers
    )


    response.raise_for_status()

    return response.json()