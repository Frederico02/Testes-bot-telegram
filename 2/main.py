import json
import time

from blaze import Blaze
from telegram import Telegram
from config import API_TOKEN, CHAT_ID, URL

if __name__ == "__main__":
    objeto_telegram = Telegram(API_TOKEN, CHAT_ID)
    objeto_blaze = Blaze(URL)

    texto = objeto_blaze.buscar_resultados()

    msg = objeto_telegram.montar_mensagem_vitoria()

    obj_msg = objeto_telegram.enviar_mensagem(msg)
    #objeto_telegram.deletar_mensagem(obj_msg.message_id)
