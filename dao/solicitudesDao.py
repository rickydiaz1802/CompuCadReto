from fastapi.encoders import jsonable_encoder
from modelos.solicitudesModelos import SolicitudesProcesos, Procesos,Salida
from dao.usuariosDao import UsuariosDAO

class SolicitudesDAO:
    def __init__(self, db):
        self.db = db

    def insertarSolicitud(self, solicitud: SolicitudesProcesos):
        salida = Salida(mensaje="")
        try:
            total = self.db.Entradas.count_documents({})
            nuevo_folio = f"CCADPRC-{total + 1:04d}"
            solicitud.folio = nuevo_folio  # Asegúrate de que el modelo tenga este campo

            result = self.db.Entradas.insert_one(jsonable_encoder(solicitud))
            salida.mensaje = "Entrada insertada con exito"
        except Exception as ex:
            print(ex)
            salida.mensaje = "Algo salió mal y no sé que"
        return salida