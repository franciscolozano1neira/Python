import random

print("Juego de adivinar la palabra \n")

palabras = [
    "python", "programa", "computadora", "teclado", "raton", "internet", "algoritmo", "variable", "codigo", "desarrollador",
    "elefante", "jirafa", "canguro", "tigre", "leon", "delfin", "camaleon", "pinguino", "cocodrilo", "ballena",
    "manzana", "banana", "naranja", "fresa", "sandia", "melocoton", "piña", "uva", "cereza", "kiwi",
    "silla", "mesa", "puerta", "ventana", "reloj", "libro", "mochila", "lapiz", "botella", "lampara",
    "españa", "francia", "mexico", "brasil", "argentina", "japon", "canada", "egipto", "madrid", "tokio"
]

palabra = random.choice(palabras)
longitud = len(palabra)

vidas = 20

print("La palabra tiene:" + str(longitud) + " letras.")

palabra_oculta = ["*"] * longitud

while vidas > 0 and "*" in palabra_oculta:
    intento = input("\nIntroduce una palabra de " + str(longitud) +  " letras: ").lower()


    if len(intento) != longitud:
        print("Debe tener exactamente" + str(longitud) + " letras.")
        vidas -= 1
        print("Vidas restantes:", vidas)
        continue

    coincidencias = 0
    for i in range(longitud):
        if intento[i] == palabra[i]:
            palabra_oculta[i] = intento[i]
            coincidencias += 1

    if coincidencias == longitud:
        print("\n¡Felicidades! Adivinaste la palabra:", palabra)
        print("Vidas restantes:", vidas)
        break
    else:
        vidas -= 1
        print("Coincidencias en posición correcta:", coincidencias)
        print("Palabra hasta ahora:", " ".join(palabra_oculta))
        print("Vidas restantes:", vidas)

if "*" in palabra_oculta:
    print("\nTe quedaste sin vidas. La palabra era:", palabra)
