from modelo.punto import Punto

mi_punto= Punto()
print("Las coordenadas del punto son: ",mi_punto.mostrar())
mi_punto.mover(10,10)
print("Las coordenadas del punto son: ",mi_punto.mostrar2())
print("La distancia es: ",mi_punto.distancia())
