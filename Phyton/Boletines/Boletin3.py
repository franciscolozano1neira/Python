#1
"""
while True:
    ps1 = input("Introduce tu contraseña:")
    ps2 = input("Introduce de nuevo la contraseña:")

    if ps1==ps2 :
        print("Las contrsaseñas son iguales")
        break
    else :
        print("Las contrsaseñas no son iguales")
        continue
print("Fin del programa")
"""
from itertools import count

"""
#2
Cont = 0 # Los contadores se inician fuera del bucle while por qe sino cada vez que pasa se reinicia a 0

while True:
    ps1 = input("Introduce tu contraseña:")
    ps2 = input("Introduce de nuevo la contraseña:")

    if ps1==ps2 :
        print("Las contrsaseñas son iguales")
        break
    else :
        Cont += 1
        print("Las contrsaseñas no son iguales")
        continue
print("Fin del programa.","Numero de intentos:",Cont)
"""
#3
"""
nombre  = input("Introduce Nombre:")
apellidos = input("Introduce Apellido:")
print(apellidos,",",nombre)
"""

#1.1
"""
Cadena = input("Escribe lo que quieras: ")
cuenta = Cadena.count(" ")
texto = Cadena.replace(" ","")
print(texto, cuenta)
"""
#2.2
"""
cadena =  input("Escriba su texto: ")
revescadena=cadena.join(reversed(cadena))
print(cadena[::-1])

#3.3
#5
Cadena=input("Escribe lo que quieras: ")
texto=Cadena.replace("a","")
texto1=texto.replace("e","")
texto2=texto1.replace("u","")
texto3=texto2.replace("i","")
texto4=texto3.replace("o","")
texto5=texto4.replace("A","")
texto6=texto5.replace("E","")
texto7=texto6.replace("U","")
texto8=texto7.replace("I","")
texto9=texto8.replace("O","")
print(texto9)

for i in Cadena:
  """"""


"""
#nif o nie

doc = input("Escriba su Documento de identidad: ").strip().upper()
letras="TRWAGMYFPDXBNJZSQVHLCKE"

if len(doc)!=9:
    print("El documento no es valido (tiene que tener minimo 9 caracteres)")
elif doc[0].isdigit():
     numero=doc[:-1]
     letra=doc[-1]
     if numero.isdigit():
         num_int=int(numero)
         letraCorrecta = letras[num_int%23]
         if letra==letraCorrecta:
             print("NIF correcto")
         else:
             print("La letra es incorrecta, la letra tiene que ser: ",letraCorrecta )
     else:
         print("No es un NIF, tiene que empezar por 8 numeros")
elif doc[0] in "XYZ":
    letraInicio=doc[0]
    numero=doc[1:-1]
    letrafin=doc[-1]
    if numero.isdigit():
        if letraInicio =="X":
            numeroCambia = "0" + numero
        elif letraInicio =="Y":
            numeroCambia = "1" + numero
        elif letraInicio == "Z":
            numeroCambia = "2" + numero

        numeroEntero = int(numeroCambia)
        letraCorrecta2=letras[numeroEntero%23]
        if letrafin==letraCorrecta2:
            print("NIE correcto")
        else:
            print("NIE incorrecto, la letra final deberia de ser: ", letraCorrecta2)
    else:
        print("Los 7 caracteres del medio tienen que ser numeros")
else:
    print("Incorrecto no empieza por X/Y/Z")


