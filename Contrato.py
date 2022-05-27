from datetime import date
from Jugador import Jugador
from Equipo import Equipo


class Contrato:
    __jugador = None
    __equipo = None
    __fechaInicio = None
    __fechaFin = None
    __pagoMensual = 0

    def __init__(self, unEquipo:Equipo, unJugador:Jugador, fechaInicio:date, fechaFin:date, pagoMensual:float):
        self.__equipo = unEquipo
        self.__jugador = unJugador
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__pagoMensual = pagoMensual
    
        
    def getJugador(self) -> Jugador:
        return self.__jugador
    
    def getEquipo(self) -> Equipo:
        return self.__equipo
    
    def getFechaInicio(self) -> date:
        return self.__fechaInicio
    
    def getFechaFin(self) -> date:
        return self.__fechaFin
    
    def getPagoMensual(self) -> float:
        return self.__pagoMensual

    def getImporteTotal(self) -> float:
        return self.__pagoMensual * ((self.getFechaFin() - self.getFechaInicio()).days//30)