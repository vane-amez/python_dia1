numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
operacion = input("Ingrese la operacion que desea realizar (+, -, *, /): ")

if operacion == "+":
  resultado = numero1 + numero2
elif operacion == "-":
  resultado = numero1 - numero2
elif operacion == "/":
  if numero2 == 0:
    resultado = "error (division por cero)"
  else:
    resultado = numero1 / numero2
elif operacion == "*":
  resultado = numero1 * numero2


print(resultado)
