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

# Criando uma funcao que vai retornar 
def tipo_derivada(tipo, funcao, x, Dx):
    # Calculando a reta secante baseado no tipo de derivada calculada
    if (tipo == "forward"):
        numerador = converter_funcao(funcao, x + Dx) - converter_funcao(funcao, x)
        denominador = Dx

    elif (tipo == "backward"):
        numerador = converter_funcao(funcao, x) - converter_funcao(funcao, x - Dx)
        denominador = Dx
        
    elif (tipo == "central"):
        numerador = converter_funcao(funcao, x + Dx) - converter_funcao(funcao, x - Dx)
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
        numerador = converter_funcao(funcao, x + 2 * Dx) - 2 * converter_funcao(funcao, x + Dx) + converter_funcao(funcao, x)
        denominador = Dx * Dx

    elif (tipo == "backward"):
        numerador = converter_funcao(funcao, x) - 2* converter_funcao(funcao, x - Dx) + converter_funcao(funcao, x - 2 * Dx)
        denominador = Dx * Dx
        
    elif (tipo == "central"):
        numerador = converter_funcao(funcao, x + Dx) - 2* converter_funcao(funcao, x) + converter_funcao(funcao, x - Dx)
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

# Testando a funcao
# Valores a serem calculados na função pedidos ao usuário
funcao = str(input("Digite a função que você deseja calcular sua derivada: "))
valor = float(input("Agora digite x: "))
Dx = float(input("Por fim, digite Dx: "))

# Escolhendo qual derivada(primeira ou segunda) será escolhida
tipo = int(input("Digite agora o tipo de derivada que você deseja calcular: \n[ 1 ] Derivada Padrão \n[ 2 ] Derivada Segunda\n"))

# Caso queiramos a derivada padrão, deixamos o usuário escolher o tipo
if (tipo == 1):
    tipo = int(input("Digite agora o método que você deseja calcular \n[ 1 ] Forward \n[ 2 ] Backward \n[ 3 ] Central"))

# Caso queiramos a derivada segunda, deixamos o usuário também escolher o tipo
elif (tipo == 2):
    tipo = int(input("Digite agora o método que você deseja calcular \n[ 1 ] Forward \n[ 2 ] Backward \n[ 3 ] Central")) + 3


print(f"A derivada da função que você deseja, com x e Dx informados é {derivacao(0.0000000001, valor, Dx, funcao, tipo)}")