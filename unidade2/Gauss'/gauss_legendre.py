# Função provisória
def funcao(x):
    return x*x

# Criando uma função para converter intervalo
def converter_intervalo(alpha, a, b):
    return ((b + a) / 2) + ((b - a) / 2) * alpha

# Função para calcular gauss-legendre
def gauss_legendre(a, b, n): # intervalo [a, b] com n pontos

    # Determinando os pesos e pontos de acordo com n para [-1, 1]
    if (n == 2):

        # Pesos
        # Repetimos alguns valores dos pesos para ser mais fácil o seu cálculo da integral
        pesos = [
            1,
            1
        ]

        # Pontos
        pontos = [
            -0.5773502692,
            0.5773502692
        ]

    elif (n == 3):

        # Pesos
        pesos = [
            0.5555555556,
            0.8888888889,
            0.5555555556
        ]

        # Pontos
        pontos = [
            -0.7745966692,
            0,
            0.7745966692
        ]

    elif (n == 4):

        # Pesos
        pesos = [
            0.3478548451,
            0.6521451549,
            0.6521451549,
            0.3478548451
        ]

        # Pontos
        pontos = [
            -0.8611363116,
            -0.3399810436,
            0.3399810436,
            0.8611363116
        ]

    # Realizando as conversões e calculando os valores
    valores_x = []
    for i in range(0, len(pontos)):
        valores_x.append(converter_intervalo(pontos[i], a, b))

    # Calculando o valor final da intergral
    valor_integral = 0
    for i in range(0, len(valores_x)):
        valor_integral += pesos[i] * funcao(valores_x[i])

    valor_integral = valor_integral * ((b - a) / 2)

    # Retornando o resultado do método
    return valor_integral
