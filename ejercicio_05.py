numero1 : int = int(input("Ingrese un numero: "))
numero2 : int = int(input("Ingrese otro numero: "))
if numero1 > numero2:
    print("El primer numero es mayor que el segundo")
elif numero2 > numero1:
    print("El segundo numero es mayor que el primero")
else:
    print("Ambos numeros son iguales")