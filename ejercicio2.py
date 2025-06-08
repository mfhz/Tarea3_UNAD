# Ejercicio 2:
# La tienda de tecnología “Byte” desea construir un programa que permita calcular el porcentaje de comisión de ventas diarias de un vendedor, acorde a los rangos de venta:
# Hasta un millón en ventas: 7%
# Más de un millón y menos de dos millones: 9%
# Más de dos millones: 11%

ventas = float(input("Ingrese el valor total de ventas diarias: "))

if ventas <= 1000000:
    comision = ventas * 0.07
    porcentaje = 7
elif ventas < 2000000:
    comision = ventas * 0.09
    porcentaje = 9
else:
    comision = ventas * 0.11
    porcentaje = 11

print(f"Porcentaje de comisión: {porcentaje}%")
print(f"Comisión a recibir: ${comision:.2f}")