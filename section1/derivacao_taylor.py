from conversor_funcao import converter_funcao

# Como as derivadas primeira e segunda foram geradas em derivacao_padrao.py
# iremos apenas calcular outras derivadas

def derivada_primeira_erro_quadratico(tipo, funcao, x, Dx):
    if (tipo == 'forward'):
        numerador = 4*converter_funcao(funcao, x+Dx) - converter_funcao(funcao, x+2*Dx) - 3*converter_funcao(funcao, x)
        denominador = 2*Dx

    if (tipo == 'backward'):
        numerador = -4*converter_funcao(funcao, x-Dx) + converter_funcao(funcao, x-2*Dx) + 3*converter_funcao(funcao, x)
        denominador = 2*Dx

    secante = numerador/denominador
    return secante

funcao = '2*x**3'
print(derivada_primeira_erro_quadratico('backward', funcao, 2, 0.000001))