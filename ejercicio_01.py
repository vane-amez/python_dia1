nombre = input("Cual es tu nombre: ")
edad = int(input("Que edad tienes: "))
if edad >= 18:
    print(nombre + " es mayor de edad.")    
elif edad < 18:
    print(nombre + " es menor de edad.")
print(nombre + " tiene " + str(edad) + " años.")    