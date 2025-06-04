from pydantic import BaseModel
from datetime import date, datetime

class Salida(BaseModel):
    mensaje: str

class SolicitudesProcesos(BaseModel):
    id_solicitud: str
    descripcion: str
    tipo_area: str
    responsable_seguimiento: str
    fecha_creacion: datetime
    fecha_estimacion: datetime
    estatus: str
    folio: str
    fecha_aprobación: datetime
    retroalimentacion: str
    aprobado_por: str

class Procesos(BaseModel):
    id_proceso: str
    nombre: str
    descripcion: str
    id_solicitud: str
    fecha_registro: datetime


