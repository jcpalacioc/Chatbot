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




