
iban = input("Introduzca su IBAN (ejemplo ES91 2100 0418 4502 0005 1332): ").strip().replace(" ", "").upper()

if len(iban)!=24:
    print("El IBAN es erroneo debe de tener 24 caracteres")
else:
    pais = iban[0:2]
    control = iban[2:4]
    entidad = iban[4:8]
    sucursal = iban[8:12]
    controlCuenta = iban [12:14]
    numeroCuenta = iban[14:24]

    print("IBAN Correcto.\n")
    print("Desglose del IBAN:")
    print("-------------------------")
    print("Código de país:          ", pais)
    print("Dígitos de control IBAN: ", control)
    print("Código de entidad:       ", entidad)
    print("Código de sucursal:      ", sucursal)
    print("Dígitos de control:      ", controlCuenta)
    print("Número de cuenta:        ", numeroCuenta)
    print("-------------------------")

    if pais != "ES":
        print("El IBAN no pertenece a España (no empieza por ES).")
    else:
        print("IBAN español detectado correctamente.")