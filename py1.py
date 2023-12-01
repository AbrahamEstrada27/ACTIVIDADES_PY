def contestarNumero():
    print("Ingresa un numero del 1 al 1000: ")
    numero = int(input())
    if numero >= 1 and numero <= 1000:
        if numero % 2 == 0:
            print("El numero " + str(numero) + " es un numero par")
        else:
            print("El numero " + str(numero) + " es un numero impar")
    else:
        print("\nERROR!!\nEl numero tiene que estar en el rango de 1 al 1000")

contestarNumero()
