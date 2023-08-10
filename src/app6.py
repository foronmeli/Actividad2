from modelo.banco import CuentaBancaria

numero_cuenta=int(input("Digite su numero de cuenta: "))
propietarios=int(input("Digite los propietarios: "))
balance=int(input("Digite el balance en el que se encuentra: "))
mi_banco=CuentaBancaria(numero_cuenta,propietarios,balance)
dinero1=int(input("Digite la cantidad de dinero ingresada: "))
mi_banco.deposito(dinero1)
dinero2=int(input("Digite la cantidad de dinero retirada: "))
mi_banco.retiro(dinero2)
print(mi_banco.mostrar_detalles(), "balanceo: ",mi_banco.balance())