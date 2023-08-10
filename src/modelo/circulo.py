import random
import random
class Circulo:

    def __init__(self,r,c,x,y,x1,y2):
        self.r=r
        self.c=c
        self.x=x
        self.y=y
        self.x1=x1
        self.y2=y2

    def perimetro(self):
        d=self.r**2
        perimetro=(2*3.1416)*d
        return perimetro
    
    def area(self):
        area=3.1416*(self.r**2)
        return area
    
    def pertenece(self):
        prueba=((self.x1-self.x)**2)+((self.y2-self.y)**2)
        r2=self.r**2
        if prueba<=r2:
            return ("El punto esta adentro")
        else:
            return ("El punto esta afuera")