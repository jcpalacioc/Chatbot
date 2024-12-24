from abc import ABC, abstractmethod


#Esta clase es abstracta y define los metodos que deben ser implementados por las clases que la hereden
class AbstractChatbot(ABC):

    @abstractmethod
    def __init__(self,Usuario):
        self.Usuario=Usuario
    
    @abstractmethod
    def EnviarMensaje(self,Mensaje):
        pass

    @abstractmethod
    def CerrarChat(self):
        pass
    