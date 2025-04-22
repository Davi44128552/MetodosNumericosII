# Importando bibliotecas necessárias
import sympy as sp

# Criando uma função para ler funções na entrada
def converter_funcao(funcao_string, valor):
    # Anotando o simbolo (no caso, x)
    x = sp.symbols('x')

    # Convertendo simbolos em equacao
    funcao = sp.sympify(funcao_string)
    funcao_numerica = funcao.subs(x, valor)

    # Retornando o resultado da funcao
    return funcao_numerica