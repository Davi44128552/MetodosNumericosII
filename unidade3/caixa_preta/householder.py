# Importando numpy para operações de álgebra linear
import numpy as np

# Criando a função para gerar a matriz de Householder
def construir_matriz_householder(A, i):
    # Definindo valores iniciais
    A = A.copy() # Cópia da matriz recebida na entrada
    n = A.shape[0] # Dimensão n da matriz
    I = np.eye(n) # Matriz identidade com as mesmas dimensões de A

    # vetores
    w = np.zeros(n)
    w_linha = np.zeros(n)

    # Definindo os valores para w
    for c in range(i + 1, n):
        w[c] = A[c][i]

    # Calculando o comprimento do vetor w
    Lw = np.linalg.norm(w)

    # Copiando Lw na posição i+1 de w'
    w_linha[i + 1] = Lw

    # Definindo o vetor N como a diferença dos valores de w e w_linha
    n = w - w_linha
    n = n / np.linalg.norm(n) # Normalizando o vetor n

    # Montando a matriz de householder
    H = I - 2 * np.outer(n, n)

    return H

# Definindo a função para gerar a tridiagonal por house holder
def tridiagonal_householder(A):
    # Definindo os valores iniciais
    A = A.copy() # Cópia da matriz de entrada
    n = A.shape[0] # Tamanho da matriz de entrada
    H = np.eye(n) # Matriz identidade com as mesmas dimensões de A
    A_anterior = A

    for i in range(0, n-2):
        # Construindo a matriz de householder
        H_i = construir_matriz_householder(A_anterior, i)

        # Realizando a transformação de similaridade com H_i gerado (Ht Ai-1 H)
        A_i = H_i.T @ A_anterior @ H_i # @ é um símbolo do python que realiza essa operação

        # Atualizando A_anterior para o próximo passo
        A_anterior = A_i

        # Acumulando as transformações -> (Hnt (... (H3t (H2t (H1t A H) H2) H3) ...) Hn)
        H = H @ H_i

    # Retornando o resultado
    return A_anterior, H
