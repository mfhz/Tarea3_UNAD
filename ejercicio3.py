# Ejercicio 3:
# En el Black Friday una tienda de tecnología va a realizar un descuento del 15% en portátiles, del 12% en cámaras y del 6% en el resto de artículos.
# Construya un programa que solicite al usuario el tipo de artículo a comprar: portátil, cámara, otros, solicite el valor del artículo y muestre el descuento y valor final a pagar.

tipo = input("Ingrese el tipo de artículo (portátil, cámara, otros): ").lower()
valor = float(input("Ingrese el valor del artículo: "))

if tipo == "portátil":
    descuento = valor * 0.15
elif tipo == "cámara":
    descuento = valor * 0.12
else:
    descuento = valor * 0.06

valor_final = valor - descuento

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Valor a pagar: ${valor_final:.2f}")