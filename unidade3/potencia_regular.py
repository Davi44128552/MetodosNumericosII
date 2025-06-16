# Importando numpy para operações com vetores
import numpy as np

# Criando a função para implementar o método da potência regular
def potencia_regular(A, v0, epsilon = 0.0001):

    # Normalizando o vetor inicial
    vetor_new = v0 / np.linalg.norm(v0, np.inf)

    # ! Obs.: Usamos o np.inf para evitar overflow

    # Definindo o erro inicial
    erro = 1

    # Definindo o lambda inicial
    lambda_old = 0

    # Realizando as iterações para recalcular os valores do autovalor e do autovetor
    while (erro > epsilon):
        # Definindo o vold
        vetor_old = vetor_new

        # Multiplicando A pelo vetor atual e depois normalizando
        Av = np.dot(A, vetor_old)
        proximo_vetor = Av / np.linalg.norm(Av, np.inf)

        # Calculando o possível autovalor dominante
        lambda_new = np.dot(vetor_new.T, np.dot(A, vetor_new))

        # Calculando o erro
        erro = abs((lambda_new - lambda_old) / lambda_new)

        # Atualizando lambda_old
        lambda_old = lambda_new

    
    # Quando enverramos o loop, retornamos o resultado
    return lambda_new, vetor_new

# Testando
A = np.array([[1, 1], [1, 1]])
v0 = np.array([1, 1])
lambda_resultante, vetor_resultante = potencia_regular(A, v0)

print(lambda_resultante)
print(vetor_resultante)