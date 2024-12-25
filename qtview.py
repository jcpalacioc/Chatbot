from PyQt6 import uic
from PyQt6.QtWidgets import QApplication,QMainWindow
from AppController import AppController
from ChatBot import Chatbot
from dotenv import load_dotenv
import os

#Esta clase es la vista de la aplicacion para el login
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

#Esta clase es la vista de la aplicacion para el panel del chat
class ChatbotView(QMainWindow):
    def __init__(self,Usuario):
        super().__init__()
        #Cargo la interfaz grafica
        uic.loadUi('src/Chat.ui', self)
        
        load_dotenv()
        API_Key = os.getenv('API_Key')

        #Crear el chatbot
        self.Chat=Chatbot(Usuario,API_Key)
        self.enviar_mss.clicked.connect(self.enviar_mensaje)
        self.cerrar_ch.clicked.connect(self.cerrar_chat)

    #Enviar un mensaje al chatbot que esta en el backend
    def enviar_mensaje(self):
        mensaje=self.txt_mensaje.text()
        respuesta=self.Chat.EnviarMensaje(mensaje)
        self.txt_chat.setText(f'{self.txt_chat.toPlainText()}\n \n Tu: {mensaje}\nBot: {respuesta}')
        self.txt_mensaje.setText('')

    #Cerrar el chat desde el boton
    def cerrar_chat(self):
        respuesta=self.Chat.CerrarChat()
        self.txt_chat.setText(f'{self.txt_chat.toPlainText()}\nBot: {respuesta}')
        self.hide()
        self.login=LoginView()
        self.login.show()
    
        
