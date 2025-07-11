import numpy as np
from potencia_regular import *
from potencia_inversa import *
from potencia_com_deslocamento import *

def main():
    A = np.array([[2, 1, 1],
              [4, -6, 0],
              [-2, 7, 2]])
    v0 = np.array([1.0, 1.0, 1.0])
    erro = 0.00001

    print("=== Potência Regular ===")
    lambda_r, vetor_r = potencia_regular(A, v0, erro)
    print("Autovalor dominante (aproximado):", lambda_r)
    print("Autovetor associado (normalizado):", vetor_r)
    print()

    print("=== Potência Inversa ===")
    lambda_i, vetor_i = potencia_inversa(A, v0, erro)
    print("Autovalor mínimo (aproximado):", lambda_i)
    print("Autovetor associado (normalizado):", vetor_i)
    print()

    deslocamento = 5
    print("=== Potência com Deslocamento ===")
    lambda_d, vetor_d = potencia_com_deslocamento(A, v0, deslocamento, erro)
    print(f"Autovalor mais próximo de {deslocamento} (aproximado):", lambda_d)
    print("Autovetor associado (normalizado):", vetor_d)
    print()

if __name__ == "__main__":
    main()
