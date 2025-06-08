# Ejercicio 4:
# La agencia de caminantes “el sendero” está otorgando descuentos en sus caminatas, acorde a la cantidad de participantes del grupo:
# De 2 a 4 personas: 12%
# De 5 a 10 personas: 17%
# Más de 10 personas: 22%
# Construya un programa que solicite la cantidad de personas y calcule el descuento correspondiente.

personas = int(input("Ingrese la cantidad de personas en el grupo: "))
valor = float(input("Ingrese el valor total de la caminata: "))

if personas >= 2 and personas <= 4:
    descuento = valor * 0.12
elif personas >= 5 and personas <= 10:
    descuento = valor * 0.17
elif personas > 10:
    descuento = valor * 0.22
else:
    descuento = 0

valor_final = valor - descuento

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Valor a pagar: ${valor_final:.2f}")