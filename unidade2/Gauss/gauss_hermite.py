# Gauss-Hermite é usado para intervalos -inf a inf

# Importando a biblioteca math
import math


# Função provisória
def funcao_exemplo(x):
    return x**2


# Função para calcular gauss-hermite
def gauss_hermite(n, funcao=funcao_exemplo):
    # Determinando os pesos e pontos
    # 2 pontos
    if n == 2:
        # Pesos
        pesos = [0.8862269255, 0.8862269255]

        # Pontos
        pontos = [-0.7071067812, 0.7071067812]

    # 3 pontos
    elif n == 3:
        # Pesos
        pesos = [0.2954089756, 1.1816359006, 0.2954089752]

        # Pontos
        pontos = [-1.2247448714, 0, 1.2247448714]

    # 4 pontos
    elif n == 4:
        # Pesos
        pesos = [0.0813128354, 0.8049140900, 0.8049140900, 0.0813128354]

        # Pontos
        pontos = [-1.6506801239, -0.5246476233, 0.52464762328, 1.65068012389]

    # Calculando o valor da integral
    valor_integral = 0
    for i in range(0, n):
        valor_integral += pesos[i] * funcao(pontos[i])

    # Retornando o valor final
    return valor_integral


# Testando a função
print(gauss_hermite(2))
print("\n", gauss_hermite(3))
print("\n", gauss_hermite(4))
