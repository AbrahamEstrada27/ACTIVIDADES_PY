def obtener_acronimo():
    # Solicitar al usuario que ingrese el significado completo
    significado_completo = input("Ingresa el significado completo: ")

    # Dividir las palabras y obtener el acrónimo
    palabras = significado_completo.split()
    acronimo = "".join(word[0].upper() for word in palabras)

    # Imprimir el acrónimo
    print("El acrónimo es: "+acronimo)

# Llamar a la función para obtener el acrónimo
obtener_acronimo()
