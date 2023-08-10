import random
class Rectangulo:

    def __init__(self):
        self.esquinax1=0
        self.esquinay1=0
        self.esquinax2=3
        self.esquinay2=3

    def perimetro(self):
        base=self.esquinax2-self.esquinax1
        altura=self.esquinay2-self.esquinay1
        perimetro=(base*2)+(altura*2)
        return perimetro

    def area(self):
        base=self.esquinax2-self.esquinax1
        altura=self.esquinay2-self.esquinay1
        area=base*altura
        return area
    
    def cuadrado(self):
        base=self.esquinax2-self.esquinax1
        altura=self.esquinay2-self.esquinay1
        if (base==altura):
            return ("El rectangulo es un cuadrado")
        else:
            return ("El rectangulo NO es un cuadrado")