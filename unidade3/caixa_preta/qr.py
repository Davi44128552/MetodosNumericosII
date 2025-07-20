# Importando numpy para operações de álgebra linear
import numpy as np
import math


# Criando uma função para realizar a soma dos quadrados dos termos abaixo da diagonal
def soma_quadrados_abaixo_diagonal(A):
    # Definindo a dimensão da matriz
    n = A.shape[0]

    # Inicializando soma como 0
    soma = 0

    # Realizando as somas
    for i in range(1, n):
        for j in range(0, i):
            # Incrementando a soma
            soma += A[i][j] ** 2

    # Retornando a soma
    return soma


# Definindo a função para construir a matriz de jacobi
def matriz_jacobi(
    A, i, j, epsilon=0.000001
):  # Defino epsilon mas o usuário podee passar
    # Definindo a dimensão da matriz
    n = A.shape[0]

    # Definindo a matriz identidade
    I = np.eye(n)

    # Verificando os casos
    if abs(A[i][j]) <= epsilon:
        return I

    # Caso a diferença entre o elemento jj da matriz A seja menor que epsilon
    if abs(A[j][j]) <= epsilon:
        # Verificando se Aij é menor ou não que 0
        if A[i][j] < 0:
            theta = math.pi / 2

        else:
            theta = -(math.pi / 2)

    # Caso contrário
    else:
        # Calculando theta
        theta = math.atan((-A[i][j]) / (A[j][j]))

    # Alterando os valores da matriz inicialmente identidade
    I[i][i] = math.cos(theta)
    I[j][j] = math.cos(theta)
    I[i][j] = math.sin(theta)
    I[j][i] = -math.sin(theta)

    # Retornando a matriz resultante
    return I


# Criando uma função para decomposição QR
def decomposicaoQR(A):
    # Definindo Rvelha, que vai ser uma cópia da matriz A
    R_anterior = A.copy()

    # Definindo as dimensões de A
    n = A.shape[0]

    # Definindo QT (Inicialmente como matriz identidade)
    QT = np.eye(n)

    # Percorrendo o loop das colunas
    for j in range(0, n - 1):
        # Percorrendo o loop das linhas
        for i in range(j + 1, n):
            # Construção da matriz de jacobi pela função anteriormente criada
            J_ij = matriz_jacobi(R_anterior, i, j)

            # Definindo o novo valor de R
            R = J_ij @ R_anterior

            # Salvando novo R para a próxima iteração
            R_anterior = R

            # Acumulando o produto das matrizes de jabobi em QT
            QT = J_ij @ QT

    # Definindo Q, que é a transposta de QT
    Q = QT.T

    # Retornando os resultados
    return Q, R


# Definindo a função do método QR
def qr(A, epsilon=0.00000001):  # Defino epsilon para caso o usuário não passe nada
    # Definindo as dimensões da matriz
    n = A.shape[0]

    # Definindo P, inicialmente como matriz identidade
    P = np.eye(n)

    # Definindo A_nova e A_velha
    A = A.copy()  # A_nova
    A_anterior = A.copy()

    # Adicionando um valor inicial para entrar no loop
    val = 1

    # Loop do erro
    while val > epsilon:
        # Recebendo Q e R como resultado da decomposição, feita anteriormente
        Q, R = decomposicaoQR(A)

        # Recalculando A como produto de R e Q
        A = R @ Q

        # Atualizando o valor de A_velha para receber A_nova
        A_anterior = A

        # Acumulando o produto das matrizes Q em P
        P = P @ Q

        # Atualizando o valor val
        val = soma_quadrados_abaixo_diagonal(A)

    # Ao sair do loop, pegamos os autovalores que são os elementos da diagonal final
    Lamb = np.diag(A)

    # Retornando os autovetores acumulados e Autovetores
    return P, Lamb
