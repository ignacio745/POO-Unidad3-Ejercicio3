import numpy as np
import csv
from Contrato import Contrato


class ManejadorContratos:
    __contratos = None
    __dimension = 0
    __cantidad = 0
    __incremento = 5
    __actual = 0

    def __init__(self):
        self.__dimension = 5
        self.__cantidad = 0
        self.__incremento = 5
        self.__contratos = np.empty(self.__dimension, dtype=Contrato)
        self.__actual = 0

    
    def agregarContrato(self, unContrato:Contrato):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = unContrato
        self.__cantidad += 1
    

    def __iter__(self):
        return self
    
    def __next__(self) -> Contrato:
        if self.__actual >= self.__cantidad:
            self.__actual = 0
            raise StopIteration
        else:
            self.__actual += 1
            return self.__contratos[self.__actual - 1]
    

    def getImporteTotal(self) -> float:
        total = 0
        for i in range(self.__cantidad):
            total += self.__contratos[i].getImporteTotal()
        return total
    

    def guardarContratos(self, nombreArchivo:str):
        archivo = open(nombreArchivo, "w")
        writer = csv.writer(archivo, delimiter=";")
        for i in range(self.__cantidad):
            unContrato:Contrato = self.__contratos[i]
            dni = unContrato.getJugador().getDNI()
            nombreEquipo = unContrato.getEquipo().getNombre()
            fechaInicio = unContrato.getFechaInicio()
            fechaFin = unContrato.getFechaFin()
            pagoMensual = unContrato.getPagoMensual()
            writer.writerow([dni, nombreEquipo, "{0}/{1}/{2}".format(fechaInicio.day, fechaInicio.month, fechaInicio.year), "{0}{1}{2}".format(fechaFin.day, fechaFin.month, fechaFin.year), pagoMensual])