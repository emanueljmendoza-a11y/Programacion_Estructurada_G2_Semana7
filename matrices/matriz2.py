matriz = []
filas = 0
columnas = 0

def pedirSize():
    global filas, columnas
    filas = int(input("Tamano de filas: "))
    columnas = int(input("Tamano de columnas: "))

def leerValor(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero")

def agregarElemento():
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            dato = leerValor(f"Valor[{i+1}, {j+1}]: ")
            matriz[i].append(dato)

def menu():
    print("""
1. Asignar tamano
2. Agregar elemento
3. Salir
""")
    op = leerValor("Ingrese una opcion: ")
    return op

def main():
    while True:
        op = menu()
        if op == 1:
            pedirSize()
        elif op == 2:
            agregarElemento()
        elif op == 3:
            print("Adios")
            break

main()