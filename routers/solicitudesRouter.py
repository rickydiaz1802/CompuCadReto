from fastapi import APIRouter, Request
from modelos.solicitudesModelos import Salida, SolicitudesProcesos, Procesos
from dao.solicitudesDao import SolicitudesDAO

router = APIRouter(
    prefix="/entradas", tags=["Entradas"])