from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ManejadorContratos import ManejadorContratos
    from Contrato import Contrato


class Equipo:
    __nombre = ""
    __ciudad = ""
    __contratos = None
    
    def __init__(self, nombre:str, ciudad:str):
        from ManejadorContratos import ManejadorContratos
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__contratos = ManejadorContratos()
    
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getCiudad(self) -> str:
        return self.__ciudad


    
    def agregarContrato(self, unContrato:Contrato):
        self.__contratos.agregarContrato(unContrato)


    def getContratosMeses(self, meses:int) -> ManejadorContratos:
        from ManejadorContratos import ManejadorContratos
        unManejadorContratos = ManejadorContratos()
        for unContrato in self.__contratos:
            if (unContrato.getFechaFin() - date.today()).days // 30 == meses:
                unManejadorContratos.agregarContrato(unContrato)
        return unManejadorContratos
    
    
    def getImporteTotal(self) -> float:
        return self.__contratos.getImporteTotal()

