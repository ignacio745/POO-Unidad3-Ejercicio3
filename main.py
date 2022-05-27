from ManejadorJugadores import ManejadorJugadores
from ManejadorEquipos import ManejadorEquipos
from ManejadorContratos import ManejadorContratos
from Menu import Menu

if __name__ == "__main__":
    unManejadorJugadores = ManejadorJugadores()
    unManejadorEquipos = ManejadorEquipos()
    unManejadoContratos = ManejadorContratos()
    unMenu = Menu()
    unManejadorEquipos.cargarArchivo("Equipos.csv")
    unMenu.ejecutarMenu(unManejadorEquipos, unManejadorJugadores, unManejadoContratos)
    unManejadoContratos.guardarContratos("Contratos.csv")