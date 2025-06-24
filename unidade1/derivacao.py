def funcao(x):
    return x**4


# Calculando as derivadas
# Derivadas Primeira
def derivada_primeira_forward(erro, x, Dx):
    if erro == "linear":
        numerador = funcao(x + Dx) - funcao(x)
        denominador = Dx

    elif erro == "quadratico":
        numerador = -funcao(x + 2 * Dx) + 4 * funcao(x + Dx) - 3 * funcao(x)
        denominador = 2 * Dx

    elif erro == "cubico":
        numerador = (
            -11 * funcao(x)
            + 18 * funcao(x + Dx)
            - 9 * funcao(x + 2 * Dx)
            + 2 * funcao(x + 3 * Dx)
        )
        denominador = 6 * Dx

    elif erro == "quarta_ordem":
        numerador = (
            -25 * funcao(x)
            + 48 * funcao(x + Dx)
            - 36 * funcao(x + 2 * Dx)
            + 16 * funcao(x + 3 * Dx)
            - 3 * funcao(x + 4 * Dx)
        )
        denominador = 12 * Dx

    return numerador / denominador


def derivada_primeira_backward(erro, x, Dx):
    if erro == "linear":
        numerador = funcao(x) - funcao(x - Dx)
        denominador = Dx

    elif erro == "quadratico":
        numerador = 3 * funcao(x) - 4 * funcao(x - Dx) + funcao(x - 2 * Dx)
        denominador = 2 * Dx

    elif erro == "cubico":
        numerador = (
            11 * funcao(x)
            - 18 * funcao(x - Dx)
            + 9 * funcao(x - 2 * Dx)
            - 2 * funcao(x - 3 * Dx)
        )
        denominador = 6 * Dx

    elif erro == "quarta_ordem":
        numerador = (
            25 * funcao(x)
            - 48 * funcao(x - Dx)
            + 36 * funcao(x - 2 * Dx)
            - 16 * funcao(x - 3 * Dx)
            + 3 * funcao(x - 4 * Dx)
        )
        denominador = 12 * Dx

    return numerador / denominador


def derivada_primeira_central(erro, x, Dx):
    if erro == "quadratico":
        numerador = funcao(x + Dx) - funcao(x - Dx)
        denominador = 2 * Dx

    elif erro == "quarta_ordem":
        numerador = (
            -funcao(x + 2 * Dx)
            + 8 * funcao(x + Dx)
            - 8 * funcao(x - Dx)
            + funcao(x - 2 * Dx)
        )
        denominador = 12 * Dx

    return numerador / denominador


# Derivadas Segunda
def derivada_segunda_forward(erro, x, Dx):
    if erro == "linear":
        numerador = funcao(x) - 2 * funcao(x + Dx) + funcao(x + 2 * Dx)
        denominador = Dx * Dx

    elif erro == "quadratico":
        numerador = (
            2 * funcao(x)
            - 5 * funcao(x + Dx)
            + 4 * funcao(x + 2 * Dx)
            - funcao(x + 3 * Dx)
        )
        denominador = Dx * Dx

    elif erro == "cubico":
        numerador = (
            35 * funcao(x)
            - 104 * funcao(x + Dx)
            + 114 * funcao(x + 2 * Dx)
            - 56 * funcao(x + 3 * Dx)
            + 11 * funcao(x + 4 * Dx)
        )
        denominador = 12 * Dx * Dx

    elif erro == "quarta_ordem":
        numerador = (
            45 * funcao(x)
            - 154 * funcao(x + Dx)
            + 214 * funcao(x + 2 * Dx)
            - 156 * funcao(x + 3 * Dx)
            + 61 * funcao(x + 4 * Dx)
            - 10 * funcao(x + 5 * Dx)
        )
        denominador = 12 * Dx * Dx

    return numerador / denominador


def derivada_segunda_backward(erro, x, Dx):
    if erro == "linear":
        numerador = funcao(x) - 2 * funcao(x - Dx) + funcao(x - 2 * Dx)
        denominador = Dx * Dx

    elif erro == "quadratico":
        numerador = (
            2 * funcao(x)
            - 5 * funcao(x - Dx)
            + 4 * funcao(x - 2 * Dx)
            - funcao(x - 3 * Dx)
        )
        denominador = Dx * Dx

    elif erro == "cubico":
        numerador = (
            35 * funcao(x)
            - 104 * funcao(x - Dx)
            + 114 * funcao(x - 2 * Dx)
            - 56 * funcao(x - 3 * Dx)
            + 11 * funcao(x - 4 * Dx)
        )
        denominador = 12 * Dx * Dx

    elif erro == "quarta_ordem":
        numerador = (
            45 * funcao(x)
            - 154 * funcao(x - Dx)
            + 214 * funcao(x - 2 * Dx)
            - 156 * funcao(x - 3 * Dx)
            + 61 * funcao(x - 4 * Dx)
            - 10 * funcao(x - 5 * Dx)
        )
        denominador = 12 * Dx * Dx

    return numerador / denominador


def derivada_segunda_central(erro, x, Dx):
    if erro == "quadratico":
        numerador = funcao(x + Dx) - 2 * funcao(x) + funcao(x - Dx)
        denominador = Dx * Dx

    elif erro == "quarta_ordem":
        numerador = (
            -funcao(x + 2 * Dx)
            + 16 * funcao(x + Dx)
            - 30 * funcao(x)
            + 16 * funcao(x - Dx)
            - funcao(x - 2 * Dx)
        )
        denominador = 12 * Dx * Dx

    return numerador / denominador


# Derivada Terceira
def derivada_terceira_forward(erro, x, Dx):
    if erro == "linear":
        numerador = (
            +funcao(x + 3 * Dx)
            - 3 * funcao(x + 2 * Dx)
            + 3 * funcao(x + Dx)
            - funcao(x)
        )
        denominador = Dx**3

    elif erro == "quadratico":
        numerador = (
            -5 * funcao(x)
            + 18 * funcao(x + Dx)
            - 24 * funcao(x + 2 * Dx)
            + 14 * funcao(x + 3 * Dx)
            - 3 * funcao(x + 4 * Dx)
        )
        denominador = 2 * Dx**3

    elif erro == "cubico":
        numerador = (
            -17 * funcao(x)
            + 71 * funcao(x + Dx)
            - 118 * funcao(x + 2 * Dx)
            + 98 * funcao(x + 3 * Dx)
            - 41 * funcao(x + 4 * Dx)
            + 7 * funcao(x + 5 * Dx)
        )
        denominador = 4 * Dx**3

    elif erro == "quarta_ordem":
        numerador = (
            -49 * funcao(x)
            + 232 * funcao(x + Dx)
            - 461 * funcao(x + 2 * Dx)
            + 496 * funcao(x + 3 * Dx)
            - 307 * funcao(x + 4 * Dx)
            + 104 * funcao(x + 5 * Dx)
            - 15 * funcao(x + 6 * Dx)
        )
        denominador = 8 * Dx**3

    return numerador / denominador


def derivada_terceira_backward(erro, x, Dx):
    if erro == "linear":
        numerador = (
            funcao(x) - 3 * funcao(x - Dx) + 3 * funcao(x - 2 * Dx) - funcao(x - 3 * Dx)
        )
        denominador = Dx**3

    elif erro == "quadratico":
        numerador = (
            5 * funcao(x)
            - 18 * funcao(x - Dx)
            + 24 * funcao(x - 2 * Dx)
            - 14 * funcao(x - 3 * Dx)
            + 3 * funcao(x - 4 * Dx)
        )
        denominador = 2 * Dx**3

    elif erro == "cubico":
        numerador = (
            -7 * funcao(x - 5 * Dx)
            + 41 * funcao(x - 4 * Dx)
            - 98 * funcao(x - 3 * Dx)
            + 118 * funcao(x - 2 * Dx)
            - 71 * funcao(x - Dx)
            + 17 * funcao(x)
        )
        denominador = 4 * Dx**3

    elif erro == "quarta_ordem":
        numerador = (
            15 * funcao(x - 6 * Dx)
            - 104 * funcao(x - 5 * Dx)
            + 307 * funcao(x - 4 * Dx)
            - 496 * funcao(x - 3 * Dx)
            + 461 * funcao(x - 2 * Dx)
            - 232 * funcao(x - Dx)
            + 49 * funcao(x)
        )
        denominador = 8 * Dx**3

    return numerador / denominador


def derivada_terceira_central(erro, x, Dx):
    if erro == "quadratico":
        numerador = (
            +funcao(x + 2 * Dx)
            - 2 * funcao(x + Dx)
            + 2 * funcao(x - Dx)
            - funcao(x - 2 * Dx)
        )
        denominador = 2 * Dx**3

    elif erro == "quarta_ordem":
        numerador = (
            -funcao(x + 3 * Dx)
            + 8 * funcao(x + 2 * Dx)
            - 13 * funcao(x + Dx)
            + 13 * funcao(x - Dx)
            - 8 * funcao(x - 2 * Dx)
            + funcao(x - 3 * Dx)
        )
        denominador = 8 * Dx**3

    return numerador / denominador


print(derivada_segunda_backward("quarta_ordem", 2, 0.00001))
