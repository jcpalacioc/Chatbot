from AbstractChatbot import AbstractChatbot
from openai import OpenAI

class OpenAIChatBot(AbstractChatbot):

    def __init__(self, Usuario,**kwargs):
        super().__init__(Usuario)
        self.__client = OpenAI()
        self._hist_mess=[]

        #CONFIG FIELDS
        self.temperature=kwargs.get('temperature',1)
        self.max_tokens=kwargs.get('max_tokens',1e5)
        self.top_p=kwargs.get('top_p',1)

        

    def EnviarMensaje(self,Mensaje):
        self._hist_mess.append(Mensaje)

        response = self.__client.chat.completions.create(
            model="gpt-4o",
            messages=self._hist_mess,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p
        )

        return response
    
    def CerrarChat(self):
        self._hist_mess=[]
        return "Chat cerrado satisfactoriamente, hasta la proxima"