import random 

opciones = ["piedra", "papel", "tijeras"]
maquina = opciones[random.randrange(0,2)]
print("******JUEGA PIEDRA PEPEL O TIJERAS******")
print ("Escribe una de las siguentes opciones: \n-piedra \n-papel \n-tijeras")
jugador = input("Tu opcion: ")

if jugador == maquina:
    print("EMPATE!!!" "\nTu Opcion: " + jugador + "  Maquina: " + maquina)
elif jugador == "piedra" and maquina == "papel":
    print("HAS PERDIDO!! \nTu Opcion: " + jugador + "  Maquina: " + maquina)
elif jugador == "piedra" and maquina == "tijeras":
     print("HAS GANADO!! \nTu Opcion: " + jugador + "  Maquina: " + maquina)
elif jugador == "papel" and maquina == "tijeras":
    print("HAS PERDIDO!! \nTu Opcion: " + jugador + "  Maquina: " + maquina)
elif jugador == "papel" and maquina == "piedra":
    print("HAS GANADO!! \nTu Opcion: " + jugador + "  Maquina: " + maquina)
elif jugador == "tijeras" and maquina == "piedra":
    print("HAS PERDIDO!! \nTu Opcion: " + jugador + "  Maquina: " + maquina)
elif jugador == "tijeras" and maquina == "papel":
    print("HAS GANADO!! \nTu Opcion: " + jugador + "  ssMaquina: " + maquina)
