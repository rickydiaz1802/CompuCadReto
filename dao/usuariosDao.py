from modelos.usuariosModelos import UsuarioSelect, UsuariosSalida
from fastapi.encoders import jsonable_encoder

class UsuariosDAO:
    def __init__(self, db):
        self.db = db

    def verificarUsuario(self, idusuario:str):
        usuario = None
        try:
            usuario = self.db.Usuarios.find_one({"_id": (idusuario)})
        except Exception as ex:
            print(ex)
        return usuario