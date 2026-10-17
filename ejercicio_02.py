# Solicita dos números, calcula su suma y resta. Indica si la suma es mayor que 10.

numero1= int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

suma = numero1 + numero2
resta = numero1 - numero2

if suma > 10:
    print("La suma es mayor que 10")
else:
    print("La suma es menor o igual que 10")
print("Resta:", resta)
print("Suma:", suma)    

