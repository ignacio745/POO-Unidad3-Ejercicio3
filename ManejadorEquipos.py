import csv
import numpy as np
from Equipo import Equipo

class ManejadorEquipos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __equipos = None

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 5
        self.__equipos = np.empty(self.__dimension, Equipo)
    
    def agregarEquipo(self, unEquipo:Equipo):
        if isinstance(unEquipo, Equipo):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__equipos.resize(self.__dimension)
            self.__equipos[self.__cantidad] = unEquipo
            self.__cantidad += 1
    
    
    def cargarArchivo(self, nombreArchivo:str):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=';')
        cantidad = int(next(reader)[0])
        self.__dimension += cantidad
        self.__equipos.resize(self.__dimension)
        contador = 0
        for fila in reader:
            contador += 1
            try:
                unEquipo = Equipo(fila[0], fila[1])
            except:
                print("[ERROR] No se pudo cargar el equipo {0}".format(contador))
            else:
                self.agregarEquipo(unEquipo)
        archivo.close()
    
    
    def buscarEquipoNombre(self, nombre: str) -> int:
        """
        Retorna el indice de un equipo en el manejador dado su nombre o -1 en caso de no encontrarse.
        
        Parametros
        ----------
        nombre : str
            El nombre del equipo a buscar
        """
        
        i = 0
        while i < self.__cantidad and self.__equipos[i].getNombre().lower() != nombre.lower():
            i += 1
        if i == self.__cantidad:
            i = -1
        return i


    def getNombresEquipos(self) -> str:
        """
        Retorna una cadena con los nombres de los equipos separados
        por saltos de linea
        """
        
        cadena = ""
        for i in range(self.__cantidad):
            cadena += "{0}\n".format(self.__equipos[i].getNombre())
        return cadena
    
    
    def getEquipoPorIndice(self, indice:int) -> Equipo:
        """
        Retorna un equipo dado su indice.

        Parametros
        ----------
        indice : int
            El indice del equipo a obtener 
        """
        assert 0 <= indice < self.__cantidad, "El indice esta fuera de rango"
        return self.__equipos[indice]
    

    
    def getEquipo(self, indice:int) -> Equipo:
        """
        Retorna un equipo dado su indice.

        Parametros
        ----------
        indice : int
            El indice del equipo en el manejador, puede obtenerse mediante
            el metodo buscarEquipoNombre
        """

        assert 0<=indice<self.__cantidad, "El indice esta fuera de rango"
        return self.__equipos[indice]