# Implementando o método de Euler (Implícito e Explícito)

# Implementando biblioteca matplotlib pra geração de visualizações e numpy para algumas operações
import matplotlib.pyplot as plt
import numpy as np

# Função teste
def pvi1(t, y):
    return (2/3) * y

# Euler explicito
def euler_explicito(funcao, t_inicial, y_inicial, h, n):

    # Definindo valor atual
    y_atual = np.array(y_inicial, dtype = float)
    
    # Inicializando os tempos
    lista_tempos = [t_inicial]

    # Inicializando os valores
    lista_valores = [y_atual.copy()]
    
    # Definindo tempo atual
    t_atual = t_inicial

    # Loop para o cálculo dos valores de y
    for i in range(0, n):

        # Calculando o próximo valor para y
        y_atual = y_atual + h * funcao(t_atual, y_atual)

        # Adicionando o novo valor para a lista de valores
        lista_valores.append(y_atual.copy())

        # Atualizando o valor do tempo e adicionando à lista
        t_atual = t_atual + h
        lista_tempos.append(t_atual)

    # Retornando as listas de valores e tempos como resultado
    return np.array(lista_valores), np.array(lista_tempos)
