from Usuario import Usuario
import bcrypt

class AppController():

    @classmethod
    def Login(cls,correo,password):
        usuario=Usuario.Obtener(correo)
        #print(usuario)
        #print(usuario.password)

        if bcrypt.checkpw(password.encode('utf-8'),usuario.password.encode('utf-8')):
            return True,usuario
        else:
            return False