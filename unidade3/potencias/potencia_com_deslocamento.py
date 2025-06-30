# Importando numpy para operações com vetores
import numpy as np

# Criando a função para implementar o método da potência regular
def potencia_inversa_com_deslocamento(A, v0, deslocamento, erro = 0.00001):

    # Normalizando o vetor inicial
    vetor = v0 / np.linalg.norm(v0, np.inf)

    # ! Obs.: Usamos o np.inf para evitar overflow

    # Definindo epsilon inicial 
    epsilon = 1

    # Definindo a matriz com deslocamento
    A_deslocada = A - deslocamento * np.eye(A.shape[0])

    # Realizando as iterações para recalcular os valores do autovalor e do autovetor
    while (epsilon > erro):
        # Resolvendo A w = vetor
        w = np.linalg.solve(A_deslocada, vetor)

        # Definindo o próximo vetor
        proximo_vetor = w / np.linalg.norm(w, np.inf)

        # Calculando o possível autovalor dominante
        lambda_atual = np.dot(proximo_vetor, np.dot(A, proximo_vetor)) / np.dot(proximo_vetor, proximo_vetor)

        # Redefinindo o valor de epsilon
        epsilon = abs(np.linalg.norm(proximo_vetor - vetor, np.inf))

        # Caso o critério de parada não tenha sido atingido, continuamos o loop
        vetor = proximo_vetor
    
    # Quando encerramos o loop, retornamos o resultado
    return lambda_atual, vetor

# Testando
A = np.array([[2, 0, 1], [0, 2, 0], [1, 0, 2]])
v0 = np.array([1, 1, 1])
lambda_resultante, vetor_resultante = potencia_inversa_com_deslocamento(A, v0, 1.8)

print(lambda_resultante)
print(vetor_resultante)