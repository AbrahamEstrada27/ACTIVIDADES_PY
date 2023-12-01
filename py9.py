concatenar1 = ""
concatenar2 = ""
concatenar3 = ""
print ("******CALCULAR PROPINA******")
total = int(input("¿Cual es el total de su cuenta?: "))
propina1 = total * .18
propina2 = total * .20
propina3 = total * .25
total1 = (round(propina1 + total))
total2 = (round(propina2 + total))
total3 = (round(propina3 + total))

personas = int(input("Cantidad de Personas: "))
aporte1 = total1 / personas
aporte2 = total2 / personas
aporte3 = total3 / personas

for i in range(personas):
    porcentaje = float(input(f"Porcentaje por Persona {i + 1}: "))
    resul = total1 * porcentaje
    concatenar1 += (f"\nPersona {i + 1}, {porcentaje}%: {resul}")

for i in range(personas):
    porcentaje = float(input(f"Porcentaje por Persona {i + 1}: "))
    resul = total2 * porcentaje
    concatenar2 += (f"\nPersona {i + 1}, {porcentaje}%: {resul}")

for i in range(personas):
    porcentaje = float(input(f"Porcentaje por Persona {i + 1}: "))
    resul = total3 * porcentaje
    concatenar3 += (f"\nPersona {i + 1}, {porcentaje}%: {resul}")
   

print ("\n----------APORTACIONES----------")
print ("Para el 18%:")
print(f"Su propina para 18%: {propina1}  TOTAL: {total1}" )
print(f"Aportacion por persona: {aporte1}" )
print("Alternativa de aporte: " + concatenar1)

print ("\nPara el 20%:")
print(f"Su propina para 20%: {propina2}  TOTAL: {total2}" )
print(f"Aportacion por persona: {aporte2}" )
print("Alternativa de aporte: " + concatenar2)

print ("\nPara el 25%:")
print(f"Su propina para 25%: {propina3}  TOTAL: {total3}" )
print(f"Aportacion por persona: {aporte3}" )
print("Alternativa de aporte: " + concatenar2)



