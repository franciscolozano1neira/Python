"""14. Escribe un programa que lea una hora por teclado en formato 24 horas (HH:MM). Tu
programa debería de decir si corresponde a la mañana (entre las 6 y las 11, ambas
inclusive), si es una hora de la tarde (entre las 12 y las 19, ambas inclusive), si es de la
noche (entre las 20 y las 23, ambas inclusive), si es de la madrugada (entre las 0 y las
5, ambas inclusive) o bien, si el formato no es correcto o no se corresponde con una
hora real (minutos de mas de 60, horas negativas o por encima de 23, etc."""
hora_input = input("Introduce la hora en formato 24h (HH:MM): ").strip()

if ":" not in hora_input:
    print("Formato incorrecto. Debe ser HH:MM")
else:
    partes = hora_input.split(":")
    if len(partes) != 2:
        print("Formato incorrecto. Debe ser HH:MM")
    else:
        try:
            horas = int(partes[0])
            minutos = int(partes[1])

            if not (0 <= horas <= 23) or not (0 <= minutos <= 59):
                print("Hora no válida.")
            else:
                if 6 <= horas <= 11:
                    print("Es por la mañana.")
                elif 12 <= horas <= 19:
                    print("Es por la tarde.")
                elif 20 <= horas <= 23:
                    print("Es de la noche.")
                else:  # 0-5
                    print("Es de la madrugada.")

        except ValueError:
            print("Formato incorrecto. Deben ser números.")



"""12. Crear un programa que lea un número de año por teclado e indique si es bisiesto o
no. Un año bisiesto es aquel que es divisible por 4, siempre y cuando no lo sea por
100. La excepción a esta regla son los años múltiplos de 400, que siempre son
bisiestos

 año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Bisiesto")
else:
    print("No bisiesto")"""