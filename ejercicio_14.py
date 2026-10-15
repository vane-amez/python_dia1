#Cajero
saldo= 500000    

while True:
    print("\n Menu del cajero")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        print(f"\nSu saldo actual es: ${saldo:,}")
        
    elif opcion == "2":
        valor_retiro = float(input("\nIngrese la cantidad a retirar: $"))
        if valor_retiro <= 0:
            print("Error: El monto debe ser mayor a cero.")
        elif valor_retiro > saldo:
            print("Error: Fondos insuficientes.")
        else:
            saldo -= valor_retiro
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:,}")
            
    elif opcion == "3":
        valor_deposito = float(input("\nIngrese la cantidad a depositar: $"))
        if valor_deposito <= 0:
            print("Error: El monto debe ser mayor a cero.")
        else:
            saldo += valor_deposito
            print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:,}")
            
    elif opcion == "4":
        print("\nGracias por usar el cajero automático. ¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
