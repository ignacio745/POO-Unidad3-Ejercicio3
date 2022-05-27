from typing import List
from Jugador import Jugador
import csv

class ManejadorJugadores:
    __jugadores = None

    def __init__(self):
        self.__jugadores:List[Jugador] = []

    
    def agregarJugador(self, unJugador:Jugador):
        if isinstance(unJugador, Jugador):
            self.__jugadores.append(unJugador)


    def buscarJugadorDni(self, dni: str) -> int:
        """
        Retorna el indice de un jugador dado su DNI
        
        Parametros
        ----------
        dni: str
            El DNI del jugador sin puntos
        """
        
        i = 0
        while i < len(self.__jugadores) and self.__jugadores[i].getDNI() != dni:
            i += 1
        if i == len(self.__jugadores):
            i = -1
        return i
    

    def getJugadorPorIndice(self, indice: int) -> Jugador:
        assert 0 <= indice < len(self.__jugadores), "El indice esta fuera de rango"
        return self.__jugadores[indice]

