# suma de matrices cuadradas
matrizA = []
matrizB = []


def imprimirMatriz(Matriz):
    for fila in Matriz:
        print(f"{fila}")


# Llenar matriz A
print("LLenar matriz A")
for i in range(3):
    matrizA.append([])
    for j in range(3):
        elemento = float(input(f"dime el valor de posicion({i}, {j}):"))
        matrizA[i].append(elemento)


print("Llenar Matriz B")
for i in range(3):
    columnas = []
    for j in range(3):
        elemento = float(input(f"Elemento ({i + 1}), ({j + 1}):"))
        columnas.append(elemento)
    matrizB.append(columnas)

MatrizC = []
for i in range(3):
    columnas = []
    for j in range(3):
        suma = matrizA[i][j] + matrizB[i][j]
        columnas.append(suma)
    MatrizC.append(columnas)


print("Mostraar Matriz A")
imprimirMatriz(matrizA)


print("Mostrar Matriz B")
imprimirMatriz(matrizB)


print("Suma de Matrices ")
imprimirMatriz(MatrizC)


