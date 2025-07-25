# Implementando o método preditor-corretor de quarta ordem

# Importando bibliotecas necessárias para o cálculo deste método
import numpy as np
import matplotlib.pyplot as plt
from runge_kutta import runge_kutta_4 as rk4 # Importando o nosso método de runge-kutta

# Função para o método
def preditor_corretor_4(funcao, t_inicial, y_inicial, h, n):

    # Chamando o runge-kutta para dar os valores de t e y
    y_rk, t_rk = rk4(funcao, t_inicial, y_inicial, h, 3)

    # Fazendo uma cópia dos resultados de rk4
    y_atual = y_rk.copy()
    t_atual = t_rk.copy()

    # Loop do método
    for i in range(3, n):

        # Preditor
        f0 = funcao(t_atual[i - 3], y_atual[i - 3])
        f1 = funcao(t_atual[i - 2], y_atual[i - 2])
        f2 = funcao(t_atual[i - 1], y_atual[i - 1])
        f3 = funcao(t_atual[i], y_atual[i])

        # Calculando os valores de y e t preditor
        y_preditor = y_atual[i] + (h / 24) * (55 * f3 - 59 * f2 + 37 * f1 - 9 * f0)
        t_preditor = t_atual[i] + h

        # Corretor
        f_preditor = funcao(t_preditor, y_preditor)
        y_corretor = y_atual[i] + (h / 24) * (9 * f_preditor + 19 * f3 - 5 * f2 + f1)

        # Atualizando os valores para y e t
        y_atual = np.append(y_atual, y_corretor)
        t_atual = np.append(t_atual, t_preditor)

    # Retornando os resultados
    return y_atual, t_atual
