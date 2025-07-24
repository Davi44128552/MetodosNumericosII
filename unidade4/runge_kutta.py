# Implementando o método de runge-kutta de ordem 4

# Importando bibliotecas que serão usadas
import numpy as np
import matplotlib.pyplot as plt

# Método de runge-kutta
def runge_kutta_4(funcao, t_inicial, y_inicial, h, n):

    # Definindo valor atual
    y_atual = np.array(y_inicial, dtype = float)
    
    # Inicializando os tempos
    lista_tempos = [t_inicial]

    # Inicializando os valores
    lista_valores = [y_atual.copy()]
    
    # Definindo tempo atual
    t_atual = t_inicial

    # Loop principal para calcular o método
    for i in range(0, n):

        # Calculando os estágios do método
        k1 = funcao(t_atual, y_atual)
        k2 = funcao(t_atual + (h / 2), y_atual + (h / 2) * k1)
        k3 = funcao(t_atual + (h / 2), y_atual + (h / 2) * k2)
        k4 = funcao(t_atual + h, y_atual + h * k3)

        # Atualizando o valor de y
        y_atual = y_atual + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        lista_valores.append(y_atual.copy())

        # Atualizando o tempo
        t_atual = t_atual + h
        lista_tempos.append(t_atual)

    # Retornando o resultado do método
    return np.array(lista_valores), np.array(lista_tempos)

