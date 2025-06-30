# Importando numpy para operações com vetores
import numpy as np

# Criando a função para implementar o método da potência regular
def potencia_regular(A, v0, erro = 0.00001):

    # Normalizando o vetor inicial
    vetor = v0 / np.linalg.norm(v0, np.inf)

    # ! Obs.: Usamos o np.inf para evitar overflow

    # Definindo epsilon inicial 
    epsilon = 1

    # Realizando as iterações para recalcular os valores do autovalor e do autovetor
    while (epsilon > erro):
        # Multiplicando A pelo vetor atual e depois normalizando
        Av = np.dot(A, vetor)
        proximo_vetor = Av / np.linalg.norm(Av, np.inf)

        # Calculando o possível autovalor dominante
        lambda_atual = np.dot(Av, vetor) / np.dot(vetor, vetor)

        # Redefinindo o valor de epsilon
        epsilon = abs(np.linalg.norm(proximo_vetor - vetor, np.inf))

        # Caso o critério de parada não tenha sido atingido, continuamos o loop
        vetor = proximo_vetor
    
    # Quando encerramos o loop, retornamos o resultado
    return lambda_atual, vetor

# Testando
A = np.array([[2, 0, 1], [0, 2, 0], [1, 0, 2]])
v0 = np.array([1, 1, 1])
lambda_resultante, vetor_resultante = potencia_regular(A, v0)

print(lambda_resultante)
print(vetor_resultante)