# Solicita el nombre del cliente, el producto, su precio y la cantidad. Calcula el subtotal y aplica estos descuentos: $500.000 o más: 15 %. $200.000 o más: 10 %. Menos de $200.000: sin descuento. Muestra una factura con el subtotal, el descuento y el total a pagar.

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

