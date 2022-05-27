from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Contrato import Contrato

class Jugador:
    __nombre = ""
    __dni = ""
    __ciudadNatal = ""
    __paisOrigen = ""
    __fechaNacimiento = None
    __contrato = None

    def __init__(self, nombre:str, dni:str, ciudadNatal:str, paisOrigen:str, fechaNacimiento:date):
        """
        Parametros
        ----------
        nombre : str 
            El nombre del jugador
        dni : str
            El dni del jugador sin puntos
        ciudadNatal : str 
            La ciudad del jugador
        paisOrigen : str 
            El pais del jugador
        fechaNacimiento : date 
            La fecha de nacimiento del jugador
        """
        
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudadNatal = ciudadNatal
        self.__paisOrigen = paisOrigen
        self.__fechaNacimiento = fechaNacimiento
        self.__contrato = None
    
    def setContrato(self, unContrato:Contrato):
        self.__contrato = unContrato
    
    def getNombre(self) -> str:
        return self.__nombre

    def getDNI(self) -> str:
        return self.__dni
    
    def getCiudadNatal(self) ->str:
        return self.__ciudadNatal
    
    def getPaisOrigen(self) -> str:
        return self.__paisOrigen
    
    def getFechaNacimiento(self) -> date:
        return self.__fechaNacimiento
    
    def getContrato(self) -> Contrato:
        return self.__contrato