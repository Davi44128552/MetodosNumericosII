# Gauss-Laguerre é usado para intervalos 0 a inf
# Como o método é basicamente igual a gauss_legendre, apenas copiei o código e alterei os pesos e pontos

# Importando a biblioteca math
import math


# Função provisória
def funcao_exemplo(x):
    return x**2


# Função para calcular gauss-laguerre
def gauss_laguerre(n, funcao=funcao_exemplo):
    # Determinando os pesos e pontos
    # 2 pontos
    if n == 2:
        # Pesos
        pesos = [0.8535533906, 0.1464466094]

        # Pontos
        pontos = [0.5857864376, 3.4142135624]

    # 3 pontos
    elif n == 3:
        # Pesos
        pesos = [0.7110930099, 0.2785177336, 0.0103892565]

        # Pontos
        pontos = [0.4157745568, 2.2942803603, 6.2899450829]

    # 4 pontos
    elif n == 4:
        # Pesos
        pesos = [0.6031541043, 0.3574186924, 0.0388879085, 0.0005392947]

        # Pontos
        pontos = [0.3225476896, 1.7457611012, 4.5366202969, 9.3950709123]

    # Calculando o valor da integral
    valor_integral = 0
    for i in range(0, n):
        valor_integral += pesos[i] * funcao(pontos[i])

    # Retornando o valor final
    return valor_integral


# Testando a função
print(gauss_laguerre(2))
print("\n", gauss_laguerre(3))
print("\n", gauss_laguerre(4))
