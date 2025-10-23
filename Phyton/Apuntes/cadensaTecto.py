
texto = "Hola Mundo"
print(len(texto)) #devuelve la longitud de la cadena texto
#for r in texto:
 #   print(r,end="")

for i in range(0,len(texto)):
    print(i," - ",texto[i],end="")


print(texto[3:8]) # con esta sintaxis puedo seleccionar framento de cadena de la primera posicion incluida y la ultima no

print(texto[:8])

print(texto[3:])

print(texto[-2])

# no se puden modificar cadenas directamnte


#numeric a cadena

cadenaNumerica = str(3456.5)
print(cadenaNumerica)


print(texto.upper()) # devuelve la cadena en mayusculas
print(texto.lower())# devuelve a minusculas
print(texto.swapcase()) # camba mayusculas a minusculas y a reves minuscculas a maysculas

print(texto.find("o"))#indica la posicion de la letra en la cadena donde aparece por primera vez si no ahi ocurrencias el resultado es -1
print(texto[2:].find("o"))#sintaxis de bocadillo

print(texto.count("o"))#devuelve el numeroo de veces uqe aparece la ocurrencia
print(texto.count("x"))

print(texto.replace("o","X"))#esto sustitulle las o por las x en la variable texto
print(texto.replace("ola","X"))
print(texto.replace("o","sadasda"))

print(texto[2:].replace("o","X"))

texto = texto[0:2] + texto[2:].replace("o","9")
print(texto)
