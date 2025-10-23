"""Escribir un programa que reciba por teclado una temperatura en cualquiera de las
tres unidades básicas (Celcius, Farenheit o Kelvin) y la devuelva en las otras dos.
Tu programa reconocerá la unidad que has usado al introducir la entrada por teclado
porque irá acompañado de una letra que lo indique. Por ejemplo, 12C, 280.57K o
98.6F"""
entrada = input("Introduce la temperatura con su unidad (por ejemplo, 25C, 98.6F o 300K): ")
entrada = entrada.strip()

valor = entrada[:-1]
unidad = entrada[-1].upper()

try:
    valor = float(valor)
except ValueError:
    print("Error: el valor numérico no es válido.")
    exit()

if unidad == "C":
    f = valor * 1.8 + 32
    k = valor + 273.15
    print(valor, "°C =", f, "°F =", k, "K")

elif unidad == "F":
    c = (valor - 32) / 1.8
    k = (valor - 32) * 5/9 + 273.15
    print(valor, "°F =", c, "°C =", k, "K")

elif unidad == "K":
    c = valor - 273.15
    f = 1.8 * (valor - 273.15) + 32
    print(valor, "K =", c, "°C =", f, "°F")

else:
    print("Error: la unidad debe ser C, F o K.")
