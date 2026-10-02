#Cadena de caracteres
nombre = "Jeremy Jose Coca GaLeano"

texto = ""

print ("Nombre: ", end=" ")
print(nombre)
print ("Texto: ", end=" ")
print(texto)

#Longitud de la cadena
print("Nombre: ", end=" ")
print(len(nombre))
print("Texto: ", end=" ")
print(len(texto))

texto += nombre
print("Nombre: ", end=" ")
print(nombre)
print("Texto: ", end=" ")
print(texto)

#Limpiar espacios
print("Nombre: ", end=" ")
print(nombre.strip())
print("Texto: ", end=" ")
print(texto.strip())

