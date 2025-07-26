import math
from Gauss.gauss_legendre import gauss_legendre as gl
from newton_cotes.newton_cotes_fechada import formula_fechada_grau_1 as ncf

# Área do retângulo
def area_retangulo(H, B, metodo):
    # Definindo uma função constante que vai ter H como retorno
    def funcao_cte(x):
        return H

    # Calculando a área por newton-cotes ou gauss-legendre, dependendo da entrada
    if metodo == "gauss-legendre":
        # Chamando gauss_legendre para calcular a área
        area = gl(
            0, B, 2, funcao=funcao_cte
        )  # Usando 2 pontos de acordo com o material no classroom

    elif metodo == "newton-cotes":
        # Chamando newton-cotes fechada para calcular a área
        area = ncf(
            0, x_fim=B, funcao=funcao_cte
        )  # Usando grau 1 de acordo com o material no classroom

    # Retornando o resultado
    return area

# Área do triângulo
def area_triangulo(H, B, C, metodo):
    # Definindo as funções a serem usadas no cálculo da área
    def f1(x):
        return (H / C) * x

    def f2(x):
        return (H / (C - B)) * (x - B)

    # Calculando a área por newton-cotes ou gauss-legendre, dependendo da entrada
    if metodo == "gauss-legendre":
        # Chamando gauss-legendre para calcular a área do triângulo
        area = gl(0, C, 2, funcao=f1) + gl(C, B, 2, funcao=f2)

    elif metodo == "newton-cotes":
        # Chamando newton-cotes para calcular a área do triângulo
        area = ncf(0, x_fim=C, funcao=f1) + ncf(C, x_fim=B, funcao=f2)

    # Retornando o resultado
    return area

# Área do trapézio
def area_trapezio(H, B, C, D, metodo):
    # Definindo as funções a serem usadas no cálculo da área
    def f1(x):
        return (H / C) * x

    def f2(x):
        return (H / (D - B)) * (x - B)

    # Calculando a área do retângulo do trapézio, caso exista
    if B > C:
        area_ret = area_retangulo(H, B - C, metodo)

    else:
        area_ret = 0

    # Calculando a área por newton-cotes ou gauss-legendre, dependendo da entrada
    if metodo == "gauss-legendre":
        # Chamando gauss-legendre para calcular a área do trapézio
        area = gl(0, C, 2, funcao=f1) + gl(B, D, 2, funcao=f2) + area_ret

    elif metodo == "newton-cotes":
        # Chamando newton-cotes para calcular a área do trapézio
        area = ncf(0, x_fim=C, funcao=f1) + ncf(B, x_fim=D, funcao=f2) + area_ret

    # Retornando o resultado
    return area

# Área do círculo
def area_circulo(R, metodo):
    # Definindo a função a ser usada para o cálculo da área do círculo
    def integrando_alpha(alpha):
        return R**2 * alpha

    # Calculando a área por newton-cotes ou por gauss-legendre de acordo com a entrada
    if metodo == "gauss-legendre":
        # Chamando gauss-legendre para calcular a área
        area = gl(0, 1, 2, funcao=integrando_alpha) * 2 * math.pi

    elif metodo == "newton-cotes":
        # Chamando newton-cotes para calcular a área
        area = ncf(0, x_fim=1, funcao=integrando_alpha) * 2 * math.pi

    # Retornando o resultado
    return area

def area_elipse(a, b, metodo):
    # Definindo função a ser usada para o cálculo da área da elipse
    def integrando_alpha(alpha):
        return alpha * a * b

    # Calculando a área por newton-cotes ou por gauss-legendre de acordo com a entrada
    if metodo == "gauss-legendre":
        # Chamando gauss-legendre para o cálculo da área
        area = gl(0, 1, 2, funcao=integrando_alpha) * 2 * math.pi

    elif metodo == "newton-cotes":
        # Chamando newton-cotes para o cálculo da área
        area = ncf(0, x_fim=1, funcao=integrando_alpha) * 2 * math.pi

    # Retornando o resultado
    return area
