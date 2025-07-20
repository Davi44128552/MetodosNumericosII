# Importando numpy para operações com vetores
import numpy as np


# Criando a função para implementar o método da potência regular
def potencia_regular(A, v0, erro=0.00001):
    # Copiando o vetor inicial
    proximo_vetor = v0

    # Definindo o lambda inicial
    lambda_atual = 0

    # Definindo epsilon inicial
    epsilon = 1

    # Realizando as iterações para recalcular os valores do autovalor e do autovetor
    while epsilon > erro:
        lambda_old = lambda_atual  # Copiando o último lambda

        # Copiando e normalizando o último vetor calculado
        vetor = proximo_vetor
        vetor = vetor / np.linalg.norm(vetor)

        # Definindo o valor para o próximo vetor
        proximo_vetor = A @ vetor

        # Calculando o possível autovalor dominante
        lambda_atual = vetor.T @ proximo_vetor

        # Redefinindo o valor de epsilon
        epsilon = abs((lambda_atual - lambda_old) / lambda_atual)

        # Caso o critério de parada não tenha sido atingido, continuamos o loop
        lambda_old = lambda_atual

    # Quando encerramos o loop, retornamos o resultado
    return lambda_atual, vetor
