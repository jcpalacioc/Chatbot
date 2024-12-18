from AbstractChatbot import AbstractChatbot

class Chatbot(AbstractChatbot):

    def EnviarMensaje(self,Mensaje):
        return "Mensaje"
    
    def CerrarChat(self):
        self.Usuario=None
        return "Chat cerrado satisfactoriamente, hasta la proxima"