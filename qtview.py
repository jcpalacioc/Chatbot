from PyQt6 import uic
from PyQt6.QtWidgets import QApplication,QMainWindow
from AppController import AppController
from ChatBot import Chatbot
from dotenv import load_dotenv
import os

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Login.ui', self)
        self.btn_iniciar_session.clicked.connect(self.iniciar_session)
    
    def iniciar_session(self):
        correo=self.txt_correo.text()
        password=self.txt_pass.text()

        login,usuario=AppController.Login(correo,password)
        if login:
            self.hide()
            self.chatbot=ChatbotView(usuario)
            self.chatbot.show()
        else:
            self.lbl_error.setText("Correo o contraseña incorrecta")

class ChatbotView(QMainWindow):
    def __init__(self,Usuario):
        super().__init__()

        uic.loadUi('src/Chat.ui', self)
        
        load_dotenv()
        API_Key = os.getenv('API_Key')

        Chatbot=Chatbot(Usuario,API_Key)
        
