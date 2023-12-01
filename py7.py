import random

maquina = random.randrange(1,50)
numero = int(input("Ingresar un numero entre 1 y 50: "))
contador = 0

while numero != maquina:
    if numero > 50:
        print("El numero ingresado esta fuera de rango")
        numero = int(input("Ingresar un numero entre 1 y 50 nuevamente: "))    
        contador += 1   
    elif numero < maquina:
            partida=input("El numero ingresado es muy bajo. ¿Desea intentarlo nuevamente? \n1-SI \n2-NO\n")
            if partida == "1":
                contador += 1
                numero = int(input("Ingresar un numero entre 1 y 50: "))
            else:
                print ("Juego Terminado!!!")
                print("Cantidad de intentos: ")
                print(contador)
                break
    elif numero > maquina:
            partida=input("El numero ingresado es muy alto. ¿Desea intentarlo nuevamente? \n1-SI \n2-NO\n")
            if partida == "1":
                contador += 1
                numero = int(input("Ingresar un numero entre 1 y 50: "))
            else:
                print ("Juego Terminado!!!")
                print("Cantidad de intentos: ")
                print(contador)
                break
if numero == maquina:
     print("FELICIDADES!!! Haz adivinado el numero correctamente")
     print("Cantidad de intentos: ")
     print(contador)

    






