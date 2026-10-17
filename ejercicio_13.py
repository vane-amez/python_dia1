# Crea un menú con las opciones de sumar, restar, multiplicar y dividir. Ejecuta la operación seleccionada y muestra el resultado.

Menu = "si"
while Menu == "si":
  proceso = int(input("suma 1 /resta 2 / multiplicar 3 / dividir 4: "))
  numero1 = float(input("Ingrese el primer número: "))
  numero2 = float(input("Ingrese el segundo número: "))

  if proceso == 1:
    suma = numero1 + numero2
    print("El resultado de la suma es: ", suma)
  elif proceso == 2:
    resta = numero1 - numero2
    print("El resultado de la resta es: ", resta)
  elif proceso == 3:
    multiplicacion = numero1 * numero2
    print("El resultado de la multiplicación es: ", multiplicacion)
  elif proceso == 4:
    if numero2 == 0:
      division = numero1 / numero2
      print("El resultado de la división es: ", division)
  else:
      print("Error: No se puede dividir entre cero.")
  Menu = input("Desea continuar: si / no: ")
