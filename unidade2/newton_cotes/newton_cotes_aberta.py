def funcao(x):
    return x*x

# Fórmula aberta newton-cotes grau 1
def formula_aberta_grau_1(x_inicio, x_fim = None, delta_x = None):
    # Se x_fim tiver sido informado, calculamos delta_x
    if (delta_x is None):
        delta_x = x_fim - x_inicio

    # Calculando o espaçamento
    h = delta_x / 3

    # Retornando a fórmula que calcula a intergral
    return (delta_x / 2) * (funcao(x_inicio + h) + funcao(x_inicio + 2*h))

# Fórmula aberta newton-cotes grau 2
def formula_aberta_grau_2(x_inicio, x_fim = None, delta_x = None):
    # Se x_fim tiver sido informado, calculamos delta_x
    if (delta_x is None):
        delta_x = x_fim - x_inicio

    # Calculando o espaçamento
    h = delta_x / 4

    # Retornando o resultado
    return ((4 * h) / 3) * ((2 * funcao(x_inicio + h)) - funcao(x_inicio + 2*h) + (2 * funcao(x_inicio + 3*h)))

# Fórmula aberta newton-cotes grau 3
def formula_aberta_grau_3(x_inicio, x_fim = None, delta_x = None):
    # Se x_fim tiver sido informado, calculamos delta_x
    if (delta_x is None):
        delta_x = x_fim - x_inicio

    # Calculando o espaçamento
    h = delta_x / 5

    # Retornando o resultado
    return ((5 * h) / 24) * ((11 * funcao(x_inicio + h)) + funcao(x_inicio + 2*h) + funcao(x_inicio + 3*h) + (11 * funcao(x_inicio + 4*h)))

def integral_final(x_inicio, x_fim, erro):
    erro_atual = float("inf")
    integral_ultima = formula_aberta_grau_3(x_inicio, x_fim = x_fim)
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
            integral_atual += formula_aberta_grau_3(a, x_fim = b)
        erro_atual = abs(integral_atual - integral_ultima)
        integral_ultima = integral_atual

    return integral_ultima, iteracoes