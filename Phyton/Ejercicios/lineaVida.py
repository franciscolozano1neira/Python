
fecha = input("Introduce tu fecha de nacimiento (por ejemplo 12/03/1990 o 20170101): ")
solo_digitos = ""

for ch in fecha:
    if ch.isdigit():
        solo_digitos += ch

if solo_digitos == "":
    print("No se ingresaron dígitos.")
else:
    while len(solo_digitos) > 1:
        suma = 0
        for d in solo_digitos:
            suma += int(d)
        solo_digitos = str(suma)

    print("Tu Dígito de la Vida es:", solo_digitos)
