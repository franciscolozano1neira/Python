text = input("Ingresa tu mensaje: ")
num = int(input("numeros de desplazamientos"))
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + num
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
info = ""

cipher = info
num2 = int(input("numero de despalamiento para desencriptar"))

for char in info:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - num2
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)



""" # Pedir texto al usuario
texto = input("Introduce el texto a encriptar: ")

# Pedir valor de cambio y asegurarse que esté entre 1 y 25
while True:
        cambio = int(input("Introduce el valor de cambio (1-25): "))
        if 1 <= cambio <= 25:
            break
        else:
            print("El número debe estar entre 1 y 25.")
    

# Variables para resultados
cifrado = ""
descifrado = ""

# Cifrar texto
for ch in texto:
    if 'a' <= ch <= 'z':  # minúsculas
        cifrado += chr((ord(ch) - ord('a') + cambio) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':  # mayúsculas
        cifrado += chr((ord(ch) - ord('A') + cambio) % 26 + ord('A'))
    else:
        cifrado += ch  # deja los demás caracteres igual

# Descifrar texto
for ch in cifrado:
    if 'a' <= ch <= 'z':  # minúsculas
        descifrado += chr((ord(ch) - ord('a') - cambio) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':  # mayúsculas
        descifrado += chr((ord(ch) - ord('A') - cambio) % 26 + ord('A'))
    else:
        descifrado += ch  # deja los demás caracteres igual

# Mostrar resultados
print("\nTexto cifrado:  ", cifrado)
print("Texto descifrado:", descifrado)
"""