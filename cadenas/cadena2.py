def nombreCompleto(nombre, apellido):

    return f"{nombre} {apellido}"

def  nombreCompletoMayusculas(nombre, apellido):

    return f"{nombre.upper()} {apellido.upper()}"

def nombreCompletoMinusculas(nombre, apellido):

    return f"{nombre.lower()} {apellido.lower()}"

def nombreCompletoCapitalizado(nombre, apellido):
    return f"{nombre.capitalize()} {apellido.capitalize()}"

def nombreCompletoTitulo(nombre, apellido):
    return f"{nombre.title()} {apellido.title()}"

def generarCorreo(nombres, apellidos):
    return f"{nombres[:4]}.{apellidos[:4]}@uamv.edu.ni"

nombres = input("Ingrese sus nombres: ")
apellido= input("Ingrese sus apellidos: ")





print(generarCorreo(nombres, apellido))
print(nombreCompleto(nombres, apellido))
print(nombreCompletoMayusculas(nombres, apellido ))
print(nombreCompletoMinusculas(nombres, apellido))
print(nombreCompletoCapitalizado(nombres, apellido))
print(nombreCompletoTitulo(nombres, apellido))  