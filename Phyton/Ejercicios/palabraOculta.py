palabra = input("Introduce la palabra a buscar: ").lower()
cadena = input("Introduce la cadena donde buscar: ").lower()

pos = 0
encontrado = True

for letra in palabra:
    pos_letra = cadena.find(letra, pos)
    if pos_letra == -1:
        encontrado = False
        break
    pos = pos_letra + 1

if encontrado:
    print("Sí, la palabra está oculta en la cadena.")
else:
    print("No, la palabra NO está oculta en la cadena.")
