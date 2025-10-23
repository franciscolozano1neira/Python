import random
"""12. Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
se superan el número máximo de intentos establecidos en 5.
numero_secreto = random.randint(1, 50)

max_intentos = 5

print("Adivina el número entre 1 y 50. Tienes", max_intentos, "intentos.")

intentos = 0

while intentos < max_intentos:
    try:
        adivinanza = int(input("Introduce tu número: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    intentos += 1

    if adivinanza == numero_secreto:
        print("¡Correcto! Has adivinado el número en", intentos, "intentos.")
        break
    elif adivinanza < numero_secreto:
        print("Te has quedado corto.")
    else:
        print("Te has pasado.")

    if intentos == max_intentos:
        print("Se han acabado los intentos. El número era:", numero_secreto)

13.Modifica el programa anterior para que el programa te de todos los intentos que
necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
lograrlo

numero_secreto = random.randint(1, 50)
intentos = 0
fallos = 0

print("Adivina el número entre 1 y 50. Intenta hasta acertar.")

while True:
    try:
        adivinanza = int(input("Introduce tu número: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    intentos += 1

    if adivinanza == numero_secreto:
        print(f"¡Correcto! Has adivinado el número en {intentos} intentos y fallaste {fallos} veces antes.")
        break
    elif adivinanza < numero_secreto:
        print("Te has quedado corto.")
        fallos += 1
    else:
        print("Te has pasado.")

    fallos += 1
14


print("¡Bienvenido al juego de adivinar el número!")

while True:  # Bucle para reiniciar el juego si el usuario quiere
    numero_secreto = random.randint(1, 50)
    intentos = 0
    fallos = 0

    print("Adivina el número entre 1 y 50. Intenta hasta acertar.")

    while True:
        try:
            adivinanza = int(input("Introduce tu número: "))
        except ValueError:
            print(" Por favor, introduce un número válido.")
            continue

        intentos += 1

        if adivinanza == numero_secreto:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos y fallaste {fallos} veces antes.")
            break
        elif adivinanza < numero_secreto:
            print("Te has quedado corto.")
        else:
            print("Te has pasado.")

        fallos += 1

    # Preguntar si quiere volver a jugar
    jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez != 's':
        print("¡Gracias por jugar!")
        break

"""
"""15 Modifica el programa anterior para que al iniciar el juego te pida dos parámetros con
objeto de cambiar la dificultad del juego: el número máximo (antes era siempre 50) o
el número de intentos posibles (antes era siempre 5)"""

print("¡Bienvenido al juego de adivinar el número!")

while True:
    while True:
        try:
            max_num = int(input("Introduce el número máximo (por ejemplo, 50): "))
            if max_num < 1:
                print("El número máximo debe ser al menos 1.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    while True:
        try:
            max_intentos = int(input("Introduce el número máximo de intentos (0 o negativo = ilimitados): "))
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    numero_secreto = random.randint(1, max_num)
    intentos = 0
    fallos = 0

    print(f"Adivina el número entre 1 y {max_num}.")

    while True:
        try:
            adivinanza = int(input("Introduce tu número: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        intentos += 1

        if adivinanza == numero_secreto:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos y fallaste {fallos} veces antes.")
            break
        elif adivinanza < numero_secreto:
            print("Te has quedado corto.")
        else:
            print("Te has pasado.")

        fallos += 1

        if max_intentos > 0 and intentos >= max_intentos:
            print(f"Se han acabado los intentos. El número era: {numero_secreto}")
            break


    jugar_otra_vez = input("¿Quieres jugar otra vez? (si/no): ").lower()
    if jugar_otra_vez != 'si':
        print("¡Gracias por jugar!")
        break
