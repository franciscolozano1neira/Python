from xml.dom.minidom import ProcessingInstruction

while True:
    ps1=input("Introduce la contraseña:")
    ps2=input("Vuelve a introducir la contraseña:")

    if ps1==ps2:
        print("Las contraseñas son iguales")
        break
    else:
        print("No coinciden, inténtalo de nuevo.")