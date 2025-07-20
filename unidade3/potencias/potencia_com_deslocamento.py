# Importando numpy para operações com vetores
import numpy as np
from potencia_inversa import *


# Criando a função para implementar o método da potência regular
def potencia_com_deslocamento(A, v0, deslocamento, erro=0.00001):
    # Definindo a dimensão da matriz A
    n = A.shape[0]

    # Criando a identidade
    I = np.eye(n)

    # Definindo A_barra que vai ser dado pela diferença entre A e o deslocamento
    A_barra = A - deslocamento * I

    # Calculando os valores para o autovalor e para o autovetor pela potencia inversa
    lambda_resultante, vetor_resultante = potencia_inversa(A_barra, v0, erro)

    # Recalculando o lambda com a diferença do deslocamento
    lambda_resultante = lambda_resultante + deslocamento

    # Os autovetores são os mesmos

    # Retornando o resultado
    return lambda_resultante, vetor_resultante
