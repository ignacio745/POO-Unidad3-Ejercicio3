from Equipo import Equipo
from Contrato import Contrato
from Jugador import Jugador
from ManejadorEquipos import ManejadorEquipos
from ManejadorContratos import ManejadorContratos
from ManejadorJugadores import ManejadorJugadores
from IngresadorTeclado import IngresadorTeclado


class Menu:
    __switcher = None
    __ingresador = None
    
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.salir
                          }
        self.__ingresador = IngresadorTeclado()
        
    

    def opcion(self, unManejadorEquipos:ManejadorEquipos, unManejadorJugadores:ManejadorJugadores, unManejadorContratos:ManejadorContratos, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1':
            func(unManejadorEquipos, unManejadorJugadores, unManejadorContratos)
        elif op == '2':
            func(unManejadorJugadores)
        elif op in ('3', '4'):
            func(unManejadorEquipos)
        elif op == '5':
            func()
        else:
            func()
    
    
    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, unManejadorEquipos:ManejadorEquipos, unManejadorJugadores:ManejadorJugadores, unManejadorContratos:ManejadorContratos):
        nombre = input("Ingrese el nombre del jugador: ")
        dni = self.__ingresador.inputRegularExpression("Ingrese el DNI sin puntos: ", "[0-9]{8,8}", "DNI invalido, reintente: ")
        ciudad = input("Ingrese su ciudad natal: ")
        paisOrigen = input("Ingrese su pais de origen: ")
        fechaNacimiento = self.__ingresador.inputFecha("Ingrese su fecha de nacimiento en el formato dd/mm/aaa: ")
        
        unJugador = Jugador(nombre, dni, ciudad, paisOrigen, fechaNacimiento)
        print("Ingrese el nombre del equipo que contratara al jugador")
        print(unManejadorEquipos.getNombresEquipos())
        nombreEquipo = input("--> ")
        indice = unManejadorEquipos.buscarEquipoNombre(nombreEquipo)
        while indice == -1:
            print("Nombre invalido, reintente")
            nombreEquipo = input("--> ")
            indice = unManejadorEquipos.buscarEquipoNombre(nombreEquipo)
        unEquipo = unManejadorEquipos.getEquipo(indice)
        
        fechaInicio = self.__ingresador.inputFecha("Ingrese la fecha de inicio del contrato en el formato dd/mm/aaaa: ")
        fechaFin = self.__ingresador.inputFecha("Ingrese la fecha de de fin del contrato: ")
        while fechaFin <= fechaInicio:
            fechaFin = self.__ingresador.inputFecha("La fecha de fin del contrato debe ser posterior a la fecha de inicio, reintente: ")
        pagoMensual = self.__ingresador.inputFloat("Ingrese el pago mensual, en caso de incluir decimales usar un punto: ")
        unContrato = Contrato(unEquipo, unJugador, fechaInicio, fechaFin, pagoMensual)
        
        unManejadorJugadores.agregarJugador(unJugador)
        unManejadorContratos.agregarContrato(unContrato)
        unEquipo.agregarContrato(unContrato)
        unJugador.setContrato(unContrato)


    def opcion2(self, unManejadorJugadores:ManejadorJugadores):
        dni = self.__ingresador.inputRegularExpression("Ingrese el DNI del jugador: ", "[0-9]{8,8}", "DNI invalido, reintente: ")
        indice = unManejadorJugadores.buscarJugadorDni(dni)
        if indice == -1:
            print("[ERROR] No se encontro el jugador con DNI {0}".format(dni))
        else:
            unJugador = unManejadorJugadores.getJugadorPorIndice(indice)
            unContrato = unJugador.getContrato()
            unEquipo = unContrato.getEquipo()
            print("Equipo: {0}".format(unEquipo.getNombre()))
            print("Fecha de finalizacion del contrato: {0:02}/{1:02}/{2:04}".format(unContrato.getFechaFin().day, unContrato.getFechaFin().month, unContrato.getFechaFin().year))

    
    
    def opcion3(self, unManejadorEquipos:ManejadorEquipos):
        print("Ingrese el nombre del equipo")
        print(unManejadorEquipos.getNombresEquipos())
        nombre = input("--> ")
        indice = unManejadorEquipos.buscarEquipoNombre(nombre)
        if indice == -1:
            print("[ERROR] No se encuentra un equipo con el nombre {0}".format(nombre))
        else:
            unEquipo = unManejadorEquipos.getEquipo(indice)
            contratos = unEquipo.getContratosMeses(6)
            print("Los jugadores del equipo {0} cuyo contrato vence en 6 meses son:".format(unEquipo.getNombre()))
            print("{0:<30}{1:<9}{2:20}{3:15}{4:10}".format("Nombre", "DNI", "Ciudad natal", "Pais de Origen", "Nacimiento"))
            for unContrato in contratos:
                unJugador = unContrato.getJugador()
                print("{0:<30}{1:<9}{2:20}{3:15}{4}/{5}/{6}:".format(unJugador.getNombre(), unJugador.getDNI(), unJugador.getCiudadNatal(), unJugador.getPaisOrigen(), unJugador.getFechaNacimiento().day, unJugador.getFechaNacimiento().month, unJugador.getFechaNacimiento().year))
    

    def opcion4(self, unManejadorEquipos:ManejadorEquipos):
        print("Ingrese el nombre del equipo: ")
        print(unManejadorEquipos.getNombresEquipos())
        nombre = input("--> ")
        indice = unManejadorEquipos.buscarEquipoNombre(nombre)
        if indice == -1:
            print("[ERROR] No se encontro un equipo con el nombre {0}".format(nombre))
        else:
            unEquipo = unManejadorEquipos.getEquipoPorIndice(indice)
            print("El importe total del equipo {0} es ${1:.2f}".format(unEquipo.getNombre(), unEquipo.getImporteTotal()))


    def ejecutarMenu(self, unManejadorEquipos:ManejadorEquipos, unManejadorJugadores:ManejadorJugadores, unManejadorContratos:ManejadorContratos):
            opcion = "0"
            while opcion != "5":
                print("Ingrese la opcion deseada")
                print("[1] Contratar un jugador")
                print("[2] Consultar jugadores contratados")
                print("[3] Consultar contratos")
                print("[4] Obtener importe de contratos")
                print("[5] Salir")
                opcion = input("--> ")  
                self.opcion(unManejadorEquipos, unManejadorJugadores, unManejadorContratos, opcion)