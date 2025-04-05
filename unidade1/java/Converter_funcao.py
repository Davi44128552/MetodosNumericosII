import sys
import sympy as sp

def converter_funcao(funcao_string, valor):
    # Anotando o simbolo (no caso, x)
    x = sp.symbols('x')

    # Convertendo simbolos em equacao
    funcao = sp.sympify(funcao_string)
    funcao_numerica = funcao.subs(x, valor)

    # Retornando o resultado
    return funcao_numerica

if __name__ == "__main__":

    # Funcao string
    funcao_string = sys.argv[1]

    # Valor a ser usado como parâmetro
    valor_x = float(sys.argv[2])
    
    # Retornando o resultado
    resultado = converter_funcao(funcao_string, valor_x)
    print(resultado)  # Saída para o Java capturar