class Punto:

    def __init__(self):
        self.x= 3
        self.y= 3
    
    def mostrar(self):
        return self.x, self.y
    
    def mover(self,x2,y2):
        self.x2= x2
        self.y2= y2

    def mostrar2(self):
        return self.x2, self.y2

    def distancia(self):
        distancia1=(self.x2 - self.x)
        distancia2=(self.y2 - self.y)
        return distancia1,distancia2