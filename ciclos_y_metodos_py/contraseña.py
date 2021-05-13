intento = str(input("Ingrese la contraseña:\n")).upper()

contra = "GATO"

while intento != contra:
    print("la contraseña no es correcta")
    intento =  str(input("Ingrese la contraseña:\n")).upper()

print("Contraseña Correcta")