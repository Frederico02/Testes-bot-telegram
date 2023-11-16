import telebot


class Telegram:
    def __init__(self, api_token, chat_id):
        self.api_token = api_token
        self.chat_id = chat_id
        self.bot = telebot.TeleBot(self.api_token)
        self.mensagens_enviadas = list()

    def deletar_mensagem(self, mensagem_id, chat_id=None):
        id = chat_id or self.chat_id
        foi_deletado = self.bot.delete_message(chat_id=id, message_id=mensagem_id)
        return foi_deletado

    def enviar_mensagem(self, texto):
        msg_obj = self.bot.send_message(self.chat_id, texto)
        self.mensagens_enviadas.append(msg_obj)
        return msg_obj

    def montar_mensagem_vitoria(self, texto=None):
        if texto:
            msg = f"""
            ✅✅✅✅ VITORIA!!! ✅✅✅✅
            último resulta encontrado foi: {texto}
            """
        else:
            msg = f"""
            ✅✅✅✅ VITORIA!!! ✅✅✅✅
            """
        return msg

    def montar_mensagem_derrota(self):
        msg = f"""
        ❌❌❌❌❌ Não foi dessa vez, a estratégia falhou 😒 ! ❌❌❌❌❌
        """
        return msg
