import os
from supabase import create_client
from dotenv import load_dotenv


load_dotenv()


url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")


print("URL:", url)


supabase = create_client(url, key)


def buscar_contatos():

    resposta = (
        supabase
        .table("contatos")
        .select("*")
        .execute()
    )


    print(resposta.data)

    return resposta.data