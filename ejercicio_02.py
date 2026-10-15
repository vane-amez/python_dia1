numero1: int = int(input("Ingrese un numero: "))
numero2: int = int(input("Ingrese otro numero: "))
operacion: str = input("Ingrese la operacion que desea realizar (+, -): ")
resultado: int
if operacion == "+":
    resultado = numero1 + numero2
    if resultado > 10:
        print("El resultado es mayor que 10")
elif operacion == "-":
    resultado = numero1 - numero2
print(resultado)
