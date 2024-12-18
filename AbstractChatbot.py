from abc import ABC, abstractmethod

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
    