matriz = []
filas = 0
columnas = 0

def pedirTamaño (i ,j):
    global filas, columnas
    filas = i
    columnas = j

pedirTamaño(3, 3) 
print(filas, columnas)
    

def leerValor():
    while True:
        try:
            valor = int(input("Dime un valor numerico"))
            return valor
        except ValueError:
            print("error")

        

def agregarElemento(elemento):
 for i in range (filas):
     matriz.append([])
     for j in range (columnas):
         matriz[i].append(int(input(f"valor({i}, {j})")))


pedirTamaño(2, 2)
print(filas,  columnas )
agregarElemento()
