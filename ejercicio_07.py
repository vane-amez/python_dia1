# Solicita la edad de una persona e indica si puede ingresar a un evento para mayores de 18 años. Valida que la edad no sea negativa.

Edad = int(input("Ingrese su edad: "))

if Edad >= 18:
    print("Usted es mayor de edad puede ingresar al evento")
elif Edad < 0:
    print("La edad no puede ser negativa")
else:
    print("Usted es menor de edad no puede ingresar al evento") 
