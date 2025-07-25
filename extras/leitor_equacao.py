from sympy import sympify, symbols


# Criando uma funcao que vai converter uma entrada(string) em uma funcao matematica
def converter_funcao(funcao_string):
    # Lendo a string como uma expressão matemática onde x vai ser a variável
    x = symbols("x")
    expr = sympify(funcao_string)

    # Criando uma função a partir da expressão
    funcao = lambda x: expr.subs("x", x).evalf()

    # Retornando a funcao
    return funcao


# Testando a funcao
funcao_string = "x**3 + 5*x**2 + 11*x - 24"
funcao = converter_funcao(funcao_string)
print(funcao(1))
