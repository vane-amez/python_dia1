nombre_cliente = input("Ingrese su nombre: ")
producto = input("Ingrese el producto que desea comprar: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

subtotal = precio * cantidad
print("Subtotal: $" + str(subtotal))

if precio >= 500000:
    descuento = subtotal * 0.15
elif precio >= 200000:
    descuento = subtotal * 0.10
elif precio < 200000: 
    descuento = subtotal * 0

total = subtotal - descuento
print("Descuento: $" + str(descuento))
print("Total a pagar: $" + str(total))  

