from OpenAIChatBot import OpenAIChatBot
import pymssql
import pandas as pd
import warnings
from dotenv import load_dotenv
import os

#Esta clase hereda de OpenAIChatBot y crea un chatbot personalizado que convierte el NLP en consultas de SQL
class Chatbot(OpenAIChatBot):

    #Recibe un Usuario, Api Key y todas las posibles configuraciones del modelo GPT
    def __init__(self, Usuario,ApiKey, **kwargs):
        super().__init__(Usuario,ApiKey, **kwargs)

        informacion=self.__ObtenerInformacionSQL()
        mss={
            "role": "system",
            "content": f"Te voy a dar los siguientes pasos para que conviertas PLN en consultas a SQL Server: \n1. La base de datos contiene tablas de informacion contable y financiera tales como: la hoja de balance, el income statement, proveedores, clientes, transacciones y demas. \n2. Los nombres de las tablas y de los campos de las tablas son muy representativos, segun la peticion del usuario debes convertir el PLN en una consulta SQL que devuelva la informacion solicitada, respuesta solo en formato SQL \n3. Para lograrlo, a continuacion te muestro las tablas y campos de cada tabla de la base de datos:{informacion}\n4. Los trimestres vienen de la forma Q1,Q2,Q3 y Q4 \n5. Si la consulta del usuario no tiene nada que ver con la informacion contable o financiera proporcionada retornar (Puedes explicarte mejor?)\n6. Recuerda anidar los campos en [] para los que tienen espacios o palabras reservadas \n7. Las compras historicas se pueden pagar a los proveedores en efectivo o en cuentas por pagar"
        }
        warnings.filterwarnings("ignore")
        self._hist_mess.append(mss)

    #Se trae toda la informacion de las tablas y columnas de la base de datos
    #Retorna un String que contiene el prompt mas adecuado para el modelo
    def __ObtenerInformacionSQL(self):
        conn=pymssql.connect(server='127.0.0.1',database=self.Usuario.bbdd_name)
        cursor=conn.cursor()
        query=f"Select * from INFORMATION_SCHEMA.COLUMNS"
        cursor.execute(query)
        rows=cursor.fetchall()

        tabla_actual=""
        informacion=""
        for row in rows:
            if row[2]!=tabla_actual:
                informacion+=f'{")" if len(informacion)!=0 else ""}\n-(Tabla: {row[2]}),(CAMPOS: {row[3]}'#Nombre,Id,Correo)'
                tabla_actual=row[2]
            else:
                informacion+=','+row[3]
        informacion+=')'#para cerrar el parentesis de la ultima tabla
        conn.close()

        return informacion

    #Recibe un mensaje y lo convierte en una consulta SQL
    #Si la consulta no tiene nada que ver con la base de datos retorna un mensaje de error o de reformular la pregunta
    def EnviarMensaje(self,Mensaje):
        mss={
            "role": "user",
            "content": Mensaje
        }
        sql=super().EnviarMensaje(mss)

        if sql=='Puedes explicarte mejor?' or sql=='(Puedes explicarte mejor?)':
            return sql+' O tu pregunta esta fuera del alcance de la base de datos'
        
        respuesta=self.__traducir_sql(sql)
        print(f'Mensaje: {Mensaje}\nSQL: {sql}')
        return respuesta
    
    #Cierra el chat
    #Resetea el usuario
    def CerrarChat(self):
        self.Usuario=None
        return "Chat cerrado satisfactoriamente, hasta la proxima"
    
    #Traduce el SQL a un DataFrame para presentarlo mejor
    def __traducir_sql(self,sql):
        load_dotenv()
        PASSW = os.getenv(self.Usuario.bbdd_name+'_SQL_PASS')
        #print(self.Usuario.nombre,self.Usuario.bbdd_name+'_SQL_PASS')

        conn=pymssql.connect(
            server='127.0.0.1',database=self.Usuario.bbdd_name,user=self.Usuario.nombre,password=PASSW
        )
        cursor=conn.cursor()

        sql=sql.replace("``",'--')# Hay que formatera correctamente el sql
        query=sql
        Informacion=pd.read_sql(query,conn)
        
        return Informacion.to_string(float_format='{:f}'.format)