# Importando numpy para operações com vetores
import numpy as np
from potencia_regular import *  # Importando a potência regular


# Criando a função para implementar o método da potência regular
def potencia_inversa(A, v0, erro=0.00001):
    # Calculando a inversa da matriz A
    A_inversa = np.linalg.inv(A)

    # Chamando a função da potência regular para me dar o autovalor e autovetor da matriz inversa
    lambda_resultante, vetor_resultante = potencia_regular(A_inversa, v0, erro)

    # Calculando a inversa do lambda_resultante da matriz inversa
    # Isto porque a sua inversa é o lambda que queremos
    lambda_resultante = 1 / lambda_resultante

    # O vetor se mantém

    # Retornando o resultado final
    return lambda_resultante, vetor_resultante
