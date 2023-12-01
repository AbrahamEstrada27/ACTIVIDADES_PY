def contador():
    print("Que estas pensando?")
    pensar = str(input())
    contar = pensar.split()
    cantidad = len(contar)
    print("Hay "+str(cantidad)+" palabra/s en tu pensamiento")

contador()