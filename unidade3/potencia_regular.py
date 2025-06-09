# Importando numpy para operações com vetores
import numpy as np

# Criando a função para implementar o método da potência regular
def potencia_regular(A, v0, erro = 0.0001, max_iteracoes = 100):

    # Normalizando o vetor inicial
    vetor = v0 / np.linalg.norm(v0, np.inf)

    # ! Obs.: Usamos o np.inf para evitar overflow

    # Realizando as iterações para recalcular os valores do autovalor e do autovetor
    for i in range(0, max_iteracoes):
        # Multiplicando A pelo vetor atual e depois normalizando
        Av = np.dot(A, vetor)
        proximo_vetor = Av / np.linalg.norm(Av, np.inf)

        # Calculando o possível autovalor dominante
        lambda_atual = np.dot(Av, vetor) / np.dot(vetor, vetor)

        # Verificando a convergencia (se podemos continuar no loop ou nao)
        if (np.linalg.norm(proximo_vetor - vetor, np.inf) < erro):
            break

        # Caso o critério de parada não tenha sido atingido, continuamos o loop
        vetor = proximo_vetor

    
    # Quando enverramos o loop, retornamos o resultado
    return lambda_atual, vetor

# Testando
A = np.array([[3, 1], [1, 2]])
v0 = np.array([1, 1])
lambda_resultante, vetor_resultante = potencia_regular(A, v0)

print(lambda_resultante)
print(vetor_resultante)