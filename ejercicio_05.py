# Solicita dos números e indica cuál es mayor o si son iguales.

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if numero1 > numero2:
    print("El primer numero es mayor que el segundo")
elif numero2 > numero1:
    print("El segundo numero es mayor que el primero")
else:
    print("Ambos numeros son iguales")