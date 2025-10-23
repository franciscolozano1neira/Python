texto = input("Introduce un texto: ")
texto1 = texto.replace(" ", "").lower()

if texto1 == "":
    print("No es un palíndromo.")
else:
    if texto1 == texto1[::-1]:
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")