def datosPersonales():
    while True:
        print("Ingresa tu nombre: ")
        nombre = input()
        if nombre.isalpha() and len(nombre) > 0:
            break
        else:
            print("Ingrese su nombre correctamente y sin números")

    while True:
        print("Ingresa tu fecha de nacimiento en orden! \nEjemplo: Enero 1, 2020")
        print("Ingrese el mes : ")
        mes = input()
        print("Ingrese el día: ")
        dia = int(input())
        print("Ingrese el año (4 dígitos): ")
        anio = input()

        if nombre.isalpha() and len(nombre) > 0 and 1 <= dia <= 31 and len(anio) == 4:
            fecha = mes + " " + str(dia) + ", " + anio
            break
        else:
            print("Ingrese correctamente los datos\nDia entre 1 y 31\nAño debe tener 4 dígitos")

    while True:
        print("Ingrese su dirección correctamente! \nEjemplo: 2333 Playas, Tijuana")
        print("Ingrese el numero de casa: ")
        numCasa = int(input())
        print("Ingrese su zona: ")
        zona = input()
        print("Ingrese su ciudad: ")
        ciudad = input()

        if numCasa > 0 and len(str(numCasa)) < 5 and len(zona) > 0 and len(ciudad) > 0:
            direccion = str(numCasa) + " " + zona + ", " + ciudad
            break
        else:
            print("Ingrese correctamente los datos\nEl número de casa debe tener entre 1 y 4 dígitos")

    print("Ingrese su meta: ")
    meta = input()

    print("- Nombre: "+nombre)
    print("- Fecha de nacimiento: "+fecha)
    print("- Dirección: "+direccion)
    print("- Meta: "+meta)

datosPersonales()

