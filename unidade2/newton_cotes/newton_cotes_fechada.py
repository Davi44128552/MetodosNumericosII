import math

# Definindo função que vai ser usada para os testes
def funcao_exemplo(x):
    return x**2

# Integrais fechadas
# Integral entre dois pontos para polinômio de primeiro grau
def formula_fechada_grau_1(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Se delta_x tiver sido informado, calculamos x_fim
    elif x_fim is None:
        x_fim = x_inicio + delta_x

    # Retornando a fórmula que calcula a integral
    return (delta_x / 2) * (funcao(x_fim) + funcao(x_inicio))

def formula_fechada_grau_2(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Se delta_x tiver sido informado, calculamos x_fim
    elif x_fim is None:
        x_fim = x_inicio + delta_x

    # Definindo h: Como são 3 pontos, então dividimos delta_x ao meio
    h = delta_x / 2

    # Retornando a fórmula que calcula a intergral
    return (delta_x / 6) * (funcao(x_fim) + 4 * funcao(x_inicio + h) + funcao(x_inicio))

def formula_fechada_grau_3(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Se delta_x tiver sido informado, calculamos x_fim
    elif x_fim is None:
        x_fim = x_inicio + delta_x

    # Definindo o h: Como agora são 4 pontos, devemos dividir o delta_x em três partes
    h = delta_x / 3

    # Retornando a fórmula que calcula a integral
    return (delta_x / 8) * (
        funcao(x_inicio)
        + 3 * funcao(x_inicio + h)
        + 3 * funcao(x_inicio + 2 * h)
        + funcao(x_fim)
    )

def formula_fechada_grau_4(x_inicio, x_fim=None, delta_x=None, funcao=funcao_exemplo):
    # Se x_fim tiver sido informado, calculamos delta_x
    if delta_x is None:
        delta_x = x_fim - x_inicio

    # Se delta_x tiver sido informado, calculamos x_fim
    elif x_fim is None:
        x_fim = x_inicio + delta_x

    # Definindo o h: Como agora são 4 pontos, devemos dividir o delta_x em quatro partes
    h = delta_x / 4

    # Retornando a fórmula final
    return ((2 * h) / 45) * (
        7 * funcao(x_inicio)
        + 32 * funcao(x_inicio + h)
        + 12 * funcao(x_inicio + 2 * h)
        + 32 * funcao(x_inicio + 3 * h)
        + 7 * funcao(x_inicio + 4 * h)
    )