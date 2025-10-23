"""Un anagrama es una nueva palabra formada al reorganizar las letras de una palabra, usando todas las letras originales exactamente una vez."""
texto1 = input("Introduce el primer texto: ")
texto2 = input("Introduce el segundo texto: ")

t1 = texto1.replace(" ", "").lower()
t2 = texto2.replace(" ", "").lower()

if t1 == "" or t2 == "":
    print("Dos cadenas vacías no se consideran anagramas.")
else:

    if sorted(t1) == sorted(t2):
        print("Son anagramas.")
    else:
        print("No son anagramas.")
