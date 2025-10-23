import random

print(" Juego de adivinar la palabra \n")

palabras = [
    "python", "programa", "computadora", "teclado", "raton", "internet", "algoritmo", "variable", "codigo", "desarrollador",
    "elefante", "jirafa", "canguro", "tigre", "leon", "delfin", "camaleon", "pinguino", "cocodrilo", "ballena",
    "manzana", "banana", "naranja", "fresa", "sandia", "melocoton", "piña", "uva", "cereza", "kiwi",
    "silla", "mesa", "puerta", "ventana", "reloj", "libro", "mochila", "lapiz", "botella", "lampara",
    "españa", "francia", "mexico", "brasil", "argentina", "japon", "canada", "egipto", "madrid", "tokio"
]

palabra = random.choice(palabras)

palabra_oculta = ["_"] * len(palabra)

vidas = 10
letras_adivinadas = []

while vidas > 0 and "_" in palabra_oculta:
    print("\nPalabra:", " ".join(palabra_oculta))
    print("Vidas restantes:", vidas)
    print("Letras adivinadas:", ", ".join(letras_adivinadas))

    letra = input("Introduce una letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor introduce solo una letra.")
        continue

    if letra in letras_adivinadas:
        print("Ya has intentado esa letra.")
        vidas -= 1
        continue

    letras_adivinadas.append(letra)

    if letra in palabra:
        print("¡Correcto!")
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
    else:
        print("Letra incorrecta.")
        vidas -= 1

if "_" not in palabra_oculta:
    print("\n¡Felicidades! Adivinaste la palabra: ", palabra)
else:
    print("\nTe quedaste sin vidas. La palabra era: ", palabra)
