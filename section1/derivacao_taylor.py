from conversor_funcao import converter_funcao

# Como as derivadas primeira e segunda foram geradas em derivacao_padrao.py
# iremos apenas calcular outras derivadas

def derivada_primeira_erro_quadratico(tipo, funcao, x, Dx):
    if (tipo == 'forward'):
        numerador = 4*converter_funcao(funcao, x+Dx) - converter_funcao(funcao, x+2*Dx) - 3*converter_funcao(funcao, x)
        denominador = 2*Dx

    elif (tipo == 'backward'):
        numerador = -4*converter_funcao(funcao, x-Dx) + converter_funcao(funcao, x-2*Dx) + 3*converter_funcao(funcao, x)
        denominador = 2*Dx

    secante = numerador/denominador
    return secante

def derivada_primeira_erro_cubico(tipo, funcao, x, Dx):
    if (tipo == 'forward'):
        numerador = 18*converter_funcao(funcao, x+Dx) - 9*converter_funcao(funcao, x+2*Dx) 
        + 2*converter_funcao(funcao, x+3*Dx) - 11*converter_funcao(funcao, x)

        denominador = 6*Dx

    elif (tipo == 'backward'):
        numerador = +18*converter_funcao(funcao, x-Dx) - 9*converter_funcao(funcao, x-2*Dx) 
        + 2*converter_funcao(funcao, x-3*Dx) - 11*converter_funcao(funcao, x)

        denominador = 6*Dx

    secante = numerador/denominador
    return secante

def derivada_primeira_erro_quarta_potencia(tipo, funcao, x, Dx):
    if (tipo == 'central'):
        numerador = 8*converter_funcao(funcao, x+Dx) - 8*converter_funcao(funcao, x-Dx) - converter_funcao(funcao, x+2*Dx) + converter_funcao(funcao, x-2*Dx)

        denominador = 12 * Dx

    secante = numerador / denominador
    return secante


funcao = '2*x**3'
print(derivada_primeira_erro_quarta_potencia('central', funcao, 2, 0.000001))