import random

print("Blackjack\n")

cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

seguirJugando ="si"
victorias=0
derrotas=0
empates=0

while seguirJugando=="si":
        manoJugador = []
        manoCrupier = []

        manoJugador.append(random.choice(cartas))
        manoJugador.append(random.choice(cartas))
        manoCrupier.append(random.choice(cartas))
        manoCrupier.append(random.choice(cartas))

        valorJugador = 0
        asesJugador = 0

        for carta in manoJugador:
            if carta in ["J", "Q", "K"]:
                valorJugador += 10
            elif carta == "A":
                valorJugador += 11
                asesJugador += 1
            else:
                valorJugador += int(carta)

        while valorJugador > 21 and asesJugador > 0:
            valorJugador -= 10
            asesJugador -= 1

        valorCrupier = 0
        asesCrupier = 0

        for carta in manoCrupier:
            if carta in ["J", "Q", "K"]:
                valorCrupier += 10
            elif carta == "A":
                valorCrupier += 11
                asesCrupier += 1
            else:
                valorCrupier += int(carta)

        while valorCrupier > 21 and asesCrupier > 0:
            valorCrupier -= 10
            asesCrupier -= 1

        print("Tus cartas: ", manoJugador, "Total: ", valorJugador)
        print("Carta visible del crupier: ", manoCrupier[0])


        while valorJugador < 21:
            continua = input("¿Quieres otra carta? (si/no): ").lower()
            if continua == "si":
                nueva_carta = random.choice(cartas)
                manoJugador.append(nueva_carta)
                print("Robas: ", nueva_carta)

                if nueva_carta in ["J", "Q", "K"]:
                    valorJugador += 10
                elif nueva_carta == "A":
                    valorJugador += 11
                    asesJugador += 1
                else:
                    valorJugador += int(nueva_carta)

                while valorJugador > 21 and asesJugador > 0:
                    valorJugador -= 10
                    asesJugador -= 1

                print("Tus cartas: ", manoJugador, "Total: ", valorJugador)

                if valorJugador > 21:
                    print("Te pasaste de 21. Pierdes.")
                    break
            else:
                break

        if valorJugador <= 21:
            print("\nTurno del crupier...")
            print("Cartas del crupier: ", manoCrupier, "Total: ", valorCrupier)

            while valorCrupier < 17:
                nuevaCarta = random.choice(cartas)
                manoCrupier.append(nuevaCarta)
                print("El crupier roba: ", nuevaCarta)

                if nuevaCarta in ["J", "Q", "K"]:
                    valorCrupier += 10
                elif nuevaCarta == "A":
                    valorCrupier += 11
                    asesCrupier += 1
                else:
                    valorCrupier += int(nuevaCarta)

                while  valorCrupier > 21 and asesCrupier > 0:
                    valorCrupier -= 10
                    asesCrupier -= 1

                print("Cartas del crupier: ", manoCrupier, "Total: ", valorCrupier)

            print("\nResultado final: ")
            print("\nTus cartas: ", manoJugador, "-", valorJugador)
            print("\nCartas del crupier: ", manoCrupier, "-", valorCrupier)

            if valorCrupier > 21:
                victorias +=1
                print("\nEl crupier se pasó. ¡Ganas!")

            elif valorJugador > valorCrupier:
                victorias += 1
                print("\n¡Has ganado!")
            elif valorJugador < valorCrupier:
                derrotas +=1
                print("\nHas perdido.")
            else:
                empates+=1
                print("\nEmpate.")

        seguirJugando = input("\n¿Quieres jugar otra partida? (si/no): ").lower()

print("Victorias:", victorias)
print("Derrotas:", derrotas)
print("Empates:", empates)
