class Saldo:

    def __init__(self):
        self.dinero=[]

    def cantidad(self):
        suma=0
        for i in range (0,len(self.dinero)):
            suma=suma+self.dinero[i]
        return suma