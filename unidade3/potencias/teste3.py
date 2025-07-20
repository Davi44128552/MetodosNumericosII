import numpy as np
from potencia_regular import *
from potencia_inversa import *
from potencia_com_deslocamento import *


def main():
    # Primeira matriz resolvida na aula
    A = np.array(
        [
            [4, 2, 1, 3, 5],
            [2, 9, 3, 7, 8],
            [1, 3, 11, 6, 4],
            [3, 7, 6, 14, 7],
            [5, 8, 4, 7, 10],
        ]
    )
    v0 = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
    erro = 0.0000001

    print("========== Método da Potência Regular ==========")
    lambda_r, vetor_r = potencia_regular(A, v0, erro)
    print("Autovalor dominante (aproximado):", lambda_r)
    print("Autovetor associado (normalizado):", vetor_r)
    print()

    print("========== Método da Potência Inversa ==========")
    lambda_i, vetor_i = potencia_inversa(A, v0, erro)
    print("Autovalor mínimo (aproximado):", lambda_i)
    print("Autovetor associado (normalizado):", vetor_i)
    print()

    # Usando a potência com deslocamento para encontrar os autovalores restantes
    deslocamento = 7.5
    print("========== Potência com Deslocamento #1 ==========")
    lambda_d, vetor_d = potencia_com_deslocamento(A, v0, deslocamento, erro)
    print(f"Autovalor mais próximo de {deslocamento} (aproximado):", lambda_d)
    print("Autovetor associado (normalizado):", vetor_d)
    print()

    deslocamento = 4.8
    print("========== Potência com Deslocamento #2 ==========")
    lambda_d, vetor_d = potencia_com_deslocamento(A, v0, deslocamento, erro)
    print(f"Autovalor mais próximo de {deslocamento} (aproximado):", lambda_d)
    print("Autovetor associado (normalizado):", vetor_d)
    print()

    deslocamento = 3
    print("========== Potência com Deslocamento #3 ==========")
    lambda_d, vetor_d = potencia_com_deslocamento(A, v0, deslocamento, erro)
    print(f"Autovalor mais próximo de {deslocamento} (aproximado):", lambda_d)
    print("Autovetor associado (normalizado):", vetor_d)
    print()

    # Item c
    A_original = np.array(
        [
            [8, 4, 2, 6, 10],
            [6, 27, 9, 21, 24],
            [4, 12, 44, 24, 16],
            [15, 35, 30, 70, 35],
            [30, 48, 24, 42, 60],
        ]
    )

    lado1 = A_original @ vetor_r
    print("========== lado 1 ===========")
    print(lado1)

    B = np.array(
        [
            [2, 0, 0, 0, 0],
            [0, 3, 0, 0, 0],
            [0, 0, 4, 0, 0],
            [0, 0, 0, 5, 0],
            [0, 0, 0, 0, 6],
        ]
    )

    lado2 = lambda_r * B @ vetor_r
    print("========== lado 2 ===========")
    print(lado2)


if __name__ == "__main__":
    main()
