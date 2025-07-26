# Implementando o método euler implícito

# Importando as bibliotecas matplotlib e numpy
import matplotlib.pyplot as plt
import numpy as np


# Definindo a função f(t, y) = (2/3)*y
def f(t, y):
    return (2 / 3) * y


# Definindo a derivada df/dy = 2/3 (constante para este caso)
def dfdy(t, y):
    return 2 / 3


# Euler implícito
def euler_implicito(funcao, t_inicial, y_inicial, h, n, dfdy, erro=0.0001):
    # Definindo valor atual
    y_atual = np.array(y_inicial, dtype=float)

    # Inicializando os tempos
    lista_tempos = [t_inicial]

    # Inicializando os valores
    lista_valores = [y_atual.copy()]

    # Definindo tempo atual
    t_atual = t_inicial + h

    # Loop para o cálculo dos valores
    for i in range(0, n):
        # Definindo a função G
        def G(y):
            return y - y_atual - h * funcao(t_atual, y)

        # Calculando a derivada de G
        def dgdy(y):
            return 1 - h * dfdy(t_atual, y)

        # Chute inicial é y_atual
        # Definindo o epsilon
        y_prox = y_atual.copy()
        epsilon = 1
        while epsilon > erro:
            # Calculando o novo valor para y
            delta = G(y_prox) / dgdy(y_prox)
            y_prox = y_prox - delta

            # Redefinindo o erro
            epsilon = abs(delta)

        # Atualizando y_atual
        y_atual = y_prox

        # Adicionando os valores às listas
        lista_tempos.append(t_atual)
        lista_valores.append(y_atual.copy())

        # Redefinindo o tempo
        t_atual = t_atual + h

    # Retornando os resultados
    return np.array(lista_valores), np.array(lista_tempos)
