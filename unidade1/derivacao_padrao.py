def funcao(x):
    return x*x

# Criando uma funcao que vai retornar 
def tipo_derivada(tipo, funcao, x, Dx):
    # Calculando a reta secante baseado no tipo de derivada calculada
    if (tipo == "forward"):
        numerador = funcao(funcao, x + Dx) - funcao(funcao, x)
        denominador = Dx

    elif (tipo == "backward"):
        numerador = funcao(funcao, x) - funcao(funcao, x - Dx)
        denominador = Dx
        
    elif (tipo == "central"):
        numerador = funcao(funcao, x + Dx) - funcao(funcao, x - Dx)
        denominador = 2 * Dx

    else:
        print("Informação inválida!")
        return None
    
    # Calculando a reta secante
    secante = numerador / denominador
    return secante

# Criando a função para calcular a derivada segunda 
# Resumidamente, usa a mesma lógica da derivada simples, apenas mudando a fórmula do seu cálculo
# As induções das fórmulas finais foram dadas em aula
def tipo_derivada_segunda(tipo, funcao, x, Dx):
    # Calculando a reta secante baseado no tipo de derivada calculada
    if (tipo == "forward"):
        numerador = funcao(funcao, x + 2 * Dx) - 2 * funcao(funcao, x + Dx) + funcao(funcao, x)
        denominador = Dx * Dx

    elif (tipo == "backward"):
        numerador = funcao(funcao, x) - 2* funcao(funcao, x - Dx) + funcao(funcao, x - 2 * Dx)
        denominador = Dx * Dx
        
    elif (tipo == "central"):
        numerador = funcao(funcao, x + Dx) - 2* funcao(funcao, x) + funcao(funcao, x - Dx)
        denominador = Dx * Dx

    else:
        print("Informação inválida!")
        return None
    
    # Calculando a reta secante
    secante = numerador / denominador
    return secante

# Tentando converter strings em funcoes
def derivacao(precisao, x, Dx, funcao, tipo):

    iteracoes = 0 
    resultado_anterior = float("inf")
    loop = True
    secante = 0
    while (loop):
        # Calculando a reta secante
        # Escolhendo qual derivada calcular
        
        # Derivada padrão
        if (tipo == 1):
            secante = tipo_derivada("forward", funcao, x, Dx)
        elif (tipo == 2):
            secante = tipo_derivada("backward", funcao, x, Dx)
        elif (tipo == 3):
            secante = tipo_derivada("central", funcao, x, Dx)

        # Derivada segunda
        elif (tipo == 4):
            secante = tipo_derivada_segunda("forward", funcao, x, Dx)
        elif (tipo == 5):
            secante = tipo_derivada_segunda("backward", funcao, x, Dx)
        elif (tipo == 6):
            secante = tipo_derivada_segunda("central", funcao, x, Dx)

        # Verificando se estamos suficientemente próximos da reta tangente
        if (abs(resultado_anterior - secante) < precisao):
            loop = False

        Dx = Dx / 10 # Diminuindo o nosso DeltaX para se aproximar do real valor da derivada
        resultado_anterior = secante
    
    return secante

