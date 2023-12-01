def historia():
    print("Ingrese un nombre: ")
    nombre = str(input())
    print("Ingrese un adjetivo: ")
    adjetivo = str(input())
    print("Ingrese un pronombre: ")
    pronombre = str(input())
    print("Ingrese una accion: ")
    accion = str(input())

    historia = nombre + " era alguien muy " + adjetivo + " por eso le llamaban " + pronombre + " y le gustaba mucho " + accion

    print("\nHistoria:")
    print(historia)

historia()
