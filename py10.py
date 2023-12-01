correo = input("Ingresa tu correo electronico: ").strip()
nombre = correo[:correo.index("@")]
dominio = correo[correo.index("@")+1:]

mensaje = f"\nHOLA {nombre}! \nSe ha recibido tu respuesta con el correo {correo} con el dominio {dominio}."

print(mensaje)