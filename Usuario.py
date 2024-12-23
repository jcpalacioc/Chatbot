import bcrypt
import pymssql

class Usuario():

    def __init__(self,nombre,correo,id,password,bbdd_name):
        self.nombre=nombre
        self.correo=correo
        self.id=id
        self.password=password
        self.bbdd_name=bbdd_name

    # Encriptar la contraseña
    def __encriptar_contraseña(self,contraseña):
        # Generar una sal (salt)
        sal = bcrypt.gensalt()
        # Encriptar la contraseña
        contraseña_hash = bcrypt.hashpw(contraseña.encode('utf-8'), sal)
        return str(contraseña_hash)
    
    def Guardar(self):
        conn=pymssql.connect(server='127.0.0.1',database='Usuarios')
        cursor=conn.cursor()
        password=self.__encriptar_contraseña(self.password).replace("'","''") #Para evitar errores en la base de datos
        query=f"INSERT INTO Usuarios (nombre,correo,id,pass) VALUES ('{self.nombre}','{self.correo}','{self.id}','{password},{self.bbdd_name}')"
        
        cursor.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def Obtener(cls,correo):
        conn=pymssql.connect(server='127.0.0.1',database='Usuarios')
        cursor=conn.cursor()
        query=f"Select * from Usuarios where correo='{correo}'"
        cursor.execute(query)
        row=cursor.fetchone()

        conn.close()
        password=row[3].replace("b'","").replace("'","")
        print(password)
        return cls(row[0],row[1],row[2],password,row[4])
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nCorreo: {self.correo}\nId: {self.id}\nContraseña: {self.password}"