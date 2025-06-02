def funcao(x):
    return x*x

def derivada_primeira_erro_linear(tipo, x, Dx):
    if (tipo == 'forward'):
        numerador = funcao(x + Dx) - funcao(x)
        denominador = Dx

    elif (tipo == 'backward'):
        numerador = funcao(x) - funcao(x - Dx)
        denominador = Dx

    elif (tipo == 'central'):
        numerador = funcao(x + Dx) - funcao(x - Dx)
    
    return numerador / denominador

def derivada_primeira_erro_quadratico(tipo, x, Dx):
    if (tipo == 'forward'):
        numerador = -funcao(x + 2*Dx) + 4 * funcao(x + Dx) - 3 * funcao(x)
        denominador = 2 * Dx

    return numerador / denominador

def derivada_primeira_erro_cubico(tipo, x, Dx):
    if (tipo == 'forward'):
        numerador = - 11 * funcao(x) + 18 * funcao(x + Dx) - 9 * funcao(x + 2*Dx) + 2 * funcao(x + 3*Dx)
        denominador = 6 * Dx

    return numerador / denominador

print(derivada_primeira_erro_linear('forward', 2, 0.00001))
print(derivada_primeira_erro_quadratico('forward', 2, 0.00001))
print(derivada_primeira_erro_cubico('forward', 2, 0.00001))