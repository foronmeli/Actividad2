from modelo.carta import Carta

mi_carta=Carta()
print("Las pintas que sde puede tener son: ",mi_carta.pinta1," , ",mi_carta.pinta2," , ",mi_carta.pinta3," y ",mi_carta.pinta4)
valor=str(input("Digite el valor de su carta: "))
pinta=str(input("Digite la pinta de su carta: "))
mi_carta.cartas(valor,pinta)
print("La carta es: ",mi_carta.valor,mi_carta.pinta)