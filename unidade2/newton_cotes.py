# Definindo função que vai ser usada para os testes
def funcao(x):
    return x*x

# Integrais fechadas
# Integral entre dois pontos para polinômio de primeiro grau
def formula_fechada_grau_1(x_inicio, x_fim = None, delta_x = None):
    # Se x_fim tiver sido informado, calculamos delta_x
    if (delta_x is None):
        delta_x = x_fim - x_inicio

    # Se delta_x tiver sido informado, calculamos x_fim
    elif (x_fim is None):
        x_fim = x_inicio + delta_x

    # Retornando a fórmula que calcula a integral
    return (delta_x / 2) * (funcao(x_fim) + funcao(x_inicio))

def formula_fechada_grau_2(x_inicio, x_fim = None, delta_x = None):
    # Se x_fim tiver sido informado, calculamos delta_x
    if (delta_x is None):
        delta_x = x_fim - x_inicio

    # Se delta_x tiver sido informado, calculamos x_fim
    elif (x_fim is None):
        x_fim = x_inicio + delta_x

    # Definindo h: Como são 3 pontos, então dividimos delta_x ao meio
    h = delta_x / 2

    # Retornando a fórmula que calcula a intergrau
    return (delta_x / 6) * (funcao(x_fim) + 4*funcao(x_inicio + h) + funcao(x_inicio))

# Funcao para calcular a integral correta
def integral_final(x_inicio, x_fim, erro):
    erro_atual = float("inf")
    integral_ultima = formula_fechada_grau_2(x_inicio, x_fim = x_fim)
    n = 1
    iteracoes = 0
    while (erro_atual > erro):
        iteracoes += 1
        n *= 2
        h = (x_fim - x_inicio) / n 
        integral_atual = 0
        for i in range(n):
            a = x_inicio + i * h
            b = a + h
            integral_atual += formula_fechada_grau_2(a, x_fim = b)
        erro_atual = abs(integral_atual - integral_ultima)
        integral_ultima = integral_atual

    return integral_ultima, iteracoes
        


# Testando as integrais
print(integral_final(2, 4, 0.000001))