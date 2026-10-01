matrizA = []
k = 10


def imprimirMatriz(Matriz):
    for fila in Matriz:
        print(f"{fila}")


# Llenar matriz A
print("Llenar matriz A")
for i in range(3):
    matrizA.append([])
    for j in range(3):
        elemento = float(input(f"Posición ({i}, {j}): "))
        matrizA[i].append(elemento)

# Multiplicación por escalar k
MatrizC = []
for i in range(3):
    fila_resultado = []
    for j in range(3):
        fila_resultado.append(matrizA[i][j] * k)
    MatrizC.append(fila_resultado)

print("\nMatriz Original:")
imprimirMatriz(matrizA)

print(f"\nMatriz multiplicada por el escalar {k}:")
imprimirMatriz(MatrizC)
