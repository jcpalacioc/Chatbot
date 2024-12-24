from Usuario import Usuario
import bcrypt

#Controlador de la aplicación
class AppController():

    #Metodo para iniciar sesión
    #Recibe el correo y la contraseña
    #Retorna un booleano y el usuario si existe
    @classmethod
    def Login(cls,correo,password):
        usuario=Usuario.Obtener(correo)
        #print(usuario)
        #print(usuario.password)

        if bcrypt.checkpw(password.encode('utf-8'),usuario.password.encode('utf-8')):
            return True,usuario
        else:
            return False