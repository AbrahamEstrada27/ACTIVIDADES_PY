f = 0
igual = 0
print("******Evaluar palabras Polindromas******")
palabra = input("Ingrese una palabra: ")

for i in reversed(range(0, len(palabra))):
  if palabra[i].lower() == palabra[f].lower():
    igual += 1
  f += 1
if len(palabra) == igual:
  print("La palabra -" + palabra + "- es un palindromo!!")
else:
  print("La palabra -" + palabra + "- no es palindromo!!")
