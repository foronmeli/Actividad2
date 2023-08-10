class CuentaBancaria:

    def __init__(self,numero_cuenta,propietarios,balanceo):
        self.numero_cuenta=numero_cuenta
        self.propietarios=propietarios
        self.balanceo=balanceo
        self.depo=0
        self.reti=0
    
    def deposito(self,dinero1):
        self.depo=(self.depo+dinero1)

    def retiro(self,dinero2):
        self.reti=(self.reti-dinero2)

    def balance(self):
        self.balanceo=(self.depo-self.reti)*0.02
        return self.balanceo
    
    def mostrar_detalles(self):
        return ("Numero de cuenta: ",self.numero_cuenta," , propietarios: ", self.propietarios)