#Crea un cajero con un saldo inicial de $500.000 y estas opciones: Consultar saldo. Retirar dinero. Depositar dinero. Salir. Valida las operaciones y actualiza el saldo.

saldo= 500000 

operacion = int(input("Seleccione una operación: 1. Consultar saldo 2. Retirar dinero 3. Depositar dinero 4. Salir: "))
if operacion == 1:
    print("Su saldo actual es: $", saldo)
elif operacion == 2:
    retiro = int(input("Ingrese la cantidad a retirar: $"))
    if retiro > saldo:
        print("Saldo insuficiente. Su saldo actual es: $" + saldo)
    else:
        saldo -= retiro
        print("Retiro exitoso. Su nuevo saldo es: $", saldo)
elif operacion == 3:
    deposito = int(input("Ingrese la cantidad a depositar: $"))
    saldo += deposito
    print("Depósito exitoso. Su nuevo saldo es: $", saldo)
elif operacion == 4:
    print("Gracias por usar el cajero. Su saldo final es: $", saldo)
