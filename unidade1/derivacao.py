def funcao(x):
    return x*x

# Calculando as derivadas
# Derivadas Primeira
def derivada_primeira_erro_linear(tipo, x, Dx):
    if (tipo == 'forward'):
        numerador = funcao(x + Dx) - funcao(x)

    elif (tipo == 'backward'):
        numerador = funcao(x) - funcao(x - Dx)

    elif (tipo == 'central'):
        numerador = funcao(x + Dx) - funcao(x - Dx)
    
    return numerador / Dx

def derivada_primeira_erro_quadratico(tipo, x, Dx):
    if (tipo == 'forward'):
        numerador = -funcao(x + 2*Dx) + 4 * funcao(x + Dx) - 3 * funcao(x)

    elif (tipo == 'backward'):
        numerador = 3 * funcao(x) - 4 * funcao(x - Dx) + funcao(x - 2 * Dx)

    elif (tipo == 'central'):
        numerador = funcao(x + Dx) - funcao(x - Dx)

    return numerador / (2 * Dx)

def derivada_primeira_erro_cubico(tipo, x, Dx):
    if (tipo == 'forward'):
        numerador = - 11 * funcao(x) + 18 * funcao(x + Dx) - 9 * funcao(x + 2*Dx) + 2 * funcao(x + 3*Dx)
        denominador = 6 * Dx

    return numerador / denominador

# Derivadas Segunda
def derivada_segunda_erro_linear(tipo, x, Dx):
    if (tipo == 'forward'):
        numerador = funcao(x + 2 * Dx) - 2 * funcao(x + Dx) + funcao(x)

    elif (tipo == 'backward'):
        numerador = funcao(x) - 2 * funcao(x - Dx) + funcao(x - 2 * Dx)

    elif (tipo == 'central'):
        numerador = funcao(x + Dx) - 2 * funcao(x) + funcao(x - Dx)
        
    return numerador / (Dx * Dx)

print(derivada_primeira_erro_linear('forward', 2, 0.00001))
print(derivada_primeira_erro_quadratico('central', 2, 0.00001))
print(derivada_primeira_erro_cubico('forward', 2, 0.00001))