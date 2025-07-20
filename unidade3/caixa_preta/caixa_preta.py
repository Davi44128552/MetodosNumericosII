# Código para o método final para gerar os autovetores e autovalores
from householder import *
from qr import *


def caixa_preta(A):
    # Usando o método de householder
    A_tridiag, H = tridiagonal_householder(A)

    # Usando o método qr
    P_qr, lamb = qr(A_tridiag)

    # retornando os valores
    return np.round(lamb, 6), H @ P_qr
