# Solicita el precio de una compra: $200.000 o más: 20 % de descuento. $100.000 o más: 10 % de descuento. Menos de $100.000: sin descuento. Muestra el total a pagar.

precio_compra = float(input("Ingrese el precio de la compra: "))

if precio_compra >= 200000:
    descuento = precio_compra * 0.20
elif precio_compra >= 100000:
    descuento = precio_compra * 0.10
elif precio_compra >= 0:
    descuento = precio_compra * 0.00

precio_final = precio_compra - descuento

print("El precio final con descuento es: " + str(precio_final))

