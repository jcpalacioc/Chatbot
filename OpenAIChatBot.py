from AbstractChatbot import AbstractChatbot
from openai import OpenAI

#Crea un chatbot que utiliza la API de OpenAI para responder mensajes
class OpenAIChatBot(AbstractChatbot):

    #Recibe un Usuario y un ApiKey y parametros de configuracion del modelo GPT
    def __init__(self, Usuario,ApiKey,**kwargs):
        super().__init__(Usuario)
        self.__client = OpenAI(api_key=ApiKey)
        self._hist_mess=[]

        #CONFIG FIELDS
        self.temperature=kwargs.get('temperature',1)
        self.max_tokens=kwargs.get('max_tokens',16384)
        self.top_p=kwargs.get('top_p',1)

        
    #Recibe un mensaje y lo envia a OpenAI para obtener una respuesta
    #Guarda el mensaje en el historial de mensajes
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
    
    #Cierra el chat
    def CerrarChat(self):
        self._hist_mess=[]
        return "Chat cerrado satisfactoriamente, hasta la proxima"