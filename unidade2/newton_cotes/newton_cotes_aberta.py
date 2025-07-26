import math

def funcao_exemplo(x):
    return x**2

# Fórmula aberta newton-cotes grau 1
def formula_aberta_grau_1(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Calculando o espaçamento
    h = delta_x / 3

    # Retornando a fórmula que calcula a intergral
    return (delta_x / 2) * (funcao(x_inicio + h) + funcao(x_inicio + 2 * h))

# Fórmula aberta newton-cotes grau 2
def formula_aberta_grau_2(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Calculando o espaçamento
    h = delta_x / 4

    # Retornando o resultado
    return ((4 * h) / 3) * (
        (2 * funcao(x_inicio + h))
        - funcao(x_inicio + 2 * h)
        + (2 * funcao(x_inicio + 3 * h))
    )

# Fórmula aberta newton-cotes grau 3
def formula_aberta_grau_3(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Calculando o espaçamento
    h = delta_x / 5

    # Retornando o resultado
    return ((5 * h) / 24) * (
        (11 * funcao(x_inicio + h))
        + funcao(x_inicio + 2 * h)
        + funcao(x_inicio + 3 * h)
        + (11 * funcao(x_inicio + 4 * h))
    )

# Fórmula aberta newton-cotes grau 4
def formula_aberta_grau_4(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Calculando o espaçamento
    h = delta_x / 6

    # Retornando o resultado
    return ((6 * h) / 20) * (
        11 * funcao(x_inicio + h)
        - 14 * funcao(x_inicio + 2 * h)
        + 26 * funcao(x_inicio + 3 * h)
        - 14 * funcao(x_inicio + 4 * h)
        + 11 * funcao(x_inicio + 5 * h)
    )