import requests
import pandas as pd
import json
from SEC_API import SEC_API
from OpenAIChatBot import OpenAIChatBot
from Usuario import Usuario
import os
import pymssql
from ChatBot import Chatbot
from qtview import ChatbotView,LoginView
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow



app = QApplication(sys.argv)    
widget = LoginView()
widget.show()

sys.exit(app.exec())

# Cargar las variables del archivo .env
'''
load_dotenv()
API_Key = os.getenv('API_Key')


Chatbot=Chatbot(Usuario.Obtener('nvidia@nvidia.com'),API_Key)
#print(Chatbot.EnviarMensaje("Cuales son mis activos el primer trimestre del 2023?"))
#print(Chatbot.EnviarMensaje("Y cuales fueron para 2024?"))
#print(Chatbot.EnviarMensaje("Cual es mi inventario promedio del 2023?"))
print(Chatbot.EnviarMensaje("Cual es el cliente al que mas le he vendido?"),'\n------------------------------------------')
print(Chatbot.EnviarMensaje("Pero con el nombre"))
'''



