# Gauss-Chebyshev é usado para intervalos -1 a 1

# Importando a biblioteca math
import math


# Função provisória
def funcao_exemplo(x):
    return x**2


# Função para calcular Gauss-Chebyshev
# Já realizamos o cálculo da integral direto, sem precisar de valores armazenados
def gauss_chebyshev(n, funcao=funcao_exemplo):
    valor_integral = 0
    for i in range(1, n + 1):
        # Definindo o valor do peso
        peso = math.pi / n

        # Definindo o valor do ponto
        ponto = math.cos((2 * i - 1) * (math.pi / (2 * n)))

        # Acrescentando o valor à integral
        valor_integral += peso * funcao(ponto)

    # Retornando o resultado da integral
    return valor_integral


# Testando a função
print(gauss_chebyshev(4))
