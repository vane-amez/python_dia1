def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  if b == 0:
    return "Error: No se puede dividir entre cero."
  return a / b

def mostrar_menu():
  print("\n Calculadora")
  print("+. Sumar")
  print("-. Restar")
  print("*. Multiplicar")
  print("/. Dividir")
  print("x. Salir")

def calculadora():
  while True:
    mostrar_menu()
    opcion = input("Elige una opción (+, -, *, /, x): ")

    if opcion == "x":
      print("¡Gracias por usar la calculadora! Hasta luego.")
      break

    if opcion in ("+", "-", "*", "/"):
      try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
      except ValueError:
        print("Por favor, ingresa números válidos.")
        continue

      if opcion == "+":
        print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
      elif opcion == "-":
        print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
      elif opcion == "*":
        print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
      elif opcion == "/":
        print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
    else:
      print("Opción inválida. Por favor, selecciona una opción válida (+, -, *, /, X).")

if __name__ == "__main__":
  calculadora()