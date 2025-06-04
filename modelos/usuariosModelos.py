from pydantic import BaseModel

class Salida(BaseModel):
    mensaje: str

class UsuarioSelect(BaseModel):
    idUsuario:str
    nombre: str
    contrasena: str
    correo: str
    tipo: str

class UsuariosSalida(Salida):
    usuarios: list[UsuarioSelect]
