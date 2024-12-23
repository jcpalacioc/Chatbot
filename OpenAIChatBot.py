from AbstractChatbot import AbstractChatbot
from openai import OpenAI


class OpenAIChatBot(AbstractChatbot):

    def __init__(self, Usuario,ApiKey,**kwargs):
        super().__init__(Usuario)
        self.__client = OpenAI(api_key=ApiKey)
        self._hist_mess=[]

        #CONFIG FIELDS
        self.temperature=kwargs.get('temperature',1)
        self.max_tokens=kwargs.get('max_tokens',16384)
        self.top_p=kwargs.get('top_p',1)

        

    def EnviarMensaje(self,Mensaje):
        self._hist_mess.append(Mensaje)

        response = self.__client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self._hist_mess,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p
        )
        self._hist_mess.append({
            "role": "system",
            "content": response.choices[0].message.content
        })

        return response.choices[0].message.content
    
    def CerrarChat(self):
        self._hist_mess=[]
        return "Chat cerrado satisfactoriamente, hasta la proxima"