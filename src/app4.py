from modelo.circulo import Circulo

centro=str(input("Digite las coordenadas del centro: "))
x, y = map(int, centro.strip('()').split(','))
punto=1,6
x1,y2=punto
mi_circulo=Circulo(2,centro,x,y,x1,y2)
mi_circulo.pertenece()
print("El circulo tiene centro en: (",mi_circulo.c,") , radio: ",mi_circulo.r," , el perimetro: ",mi_circulo.perimetro()," , el area: ",mi_circulo.area())
print(mi_circulo.pertenece())