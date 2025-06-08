# Ejercicio 1:
# Para incentivar las compras, la cadena de almacenes “el triunfo” está otorgando un 15% de descuento en todos sus productos que se aplica si el valor de la compra es mayor de 300000.
# Construya un programa que permita calcular este descuento, solicitando al usuario el valor del artículo, calculando el descuento y mostrando el valor a pagar.

valor = float(input("Ingrese el valor del artículo: "))

if valor > 300000:
    descuento = valor * 0.15
    valor_final = valor - descuento
    print(f"Descuento aplicado: ${descuento:.2f}")
else:
    descuento = 0
    valor_final = valor
    print("No aplica descuento.")

print(f"Valor a pagar: ${valor_final:.2f}")