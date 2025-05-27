def funcao(x):
    return x*x

# Como as derivadas primeira e segunda foram geradas em derivacao_padrao.py
# iremos apenas calcular outras derivadas

def derivada_primeira_erro_quadratico(tipo, funcao, x, Dx):
    if (tipo == 'forward'):
        numerador = 4*funcao(funcao, x+Dx) - funcao(funcao, x+2*Dx) - 3*funcao(funcao, x)
        denominador = 2*Dx

    if (tipo == 'backward'):
        numerador = -4*funcao(funcao, x-Dx) + funcao(funcao, x-2*Dx) + 3*funcao(funcao, x)
        denominador = 2*Dx

    secante = numerador/denominador
    return secante

def derivada_primeira_erro_cubico(tipo, funcao, x, Dx):
    if (tipo == 'forward'):
        numerador = 18*funcao(funcao, x+Dx) - 9*funcao(funcao, x+2*Dx) + 2*funcao(funcao, x+3*Dx) - 11*funcao(funcao, x)
        denominador = 6*Dx

    secante = numerador/denominador
    return secante

funcao = '2*x**3'
print(derivada_primeira_erro_cubico('forward', funcao, 2, 0.000001))