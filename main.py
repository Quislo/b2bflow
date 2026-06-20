import logging

from supabase_client import buscar_contatos
from zapi_client import enviar_mensagem



logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)



def main():

    contatos = buscar_contatos()


    if not contatos:
        logging.warning("Nenhum contato encontrado")
        return



    for contato in contatos:

        nome = contato["nome"]
        telefone = contato["telefone"]


        mensagem = (
            f"Olá, {nome} tudo bem com você?"
        )


        try:

            resposta = enviar_mensagem(
                telefone,
                mensagem
            )


            logging.info(
                f"Mensagem enviada para {nome}"
            )


            print(
                f"Enviado para {nome}"
            )


        except Exception as erro:

            logging.error(
                f"Erro enviando para {nome}: {erro}"
            )

            print(
                f"Falha para {nome}"
            )



if __name__ == "__main__":
    main()