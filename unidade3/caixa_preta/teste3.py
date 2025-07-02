from householder import *
from qr import *
from caixa_preta import *

# Matriz gerada na questão 2
A = np.array([
        [4, 2, 1, 3, 5],
        [2, 9, 3, 7, 8],
        [1, 3, 11, 6, 4],
        [3, 7, 6, 14, 7],
        [5, 8, 4, 7, 10]
    ])

# Item a
print("=============================> ITEM A <=============================")

# Obtendo as matrizes H e T de householder
T, H = tridiagonal_householder(A)

# Printando
print("========== Matriz T ==========")
print(T)

print("========== Matriz H ==========")
print(H)

print("\n\n")
print("==========================================================================================")
print("\n\n")

# Item b
print("=============================> ITEM B <=============================")

# Obtendo X e Lambda pelo qr
X, LAMBDA = qr(T)

# Printando
print("========== Matriz X ==========")
print(X)

print("========== LAMBDA ==========")
print(LAMBDA)

print("\n\n")
print("==========================================================================================")
print("\n\n")

# Item c
print("=============================> ITEM C <=============================")
# A decomposição espectral é construída por A = Q LAMBDA QT

# Construindo diagonal a partir de lambda
LAMBDA_diagonal = np.diag(LAMBDA)

# Matriz dos autovetores
Autovetores = H @ X

# Decompondo
decomposicao = Autovetores @ LAMBDA_diagonal @ Autovetores.T

print("========== Lambda_diagonal ==========")
print(LAMBDA_diagonal)

print("========== Autovetores ==========")
print(Autovetores)

print("========== Resultado de C com os valores da decomposição ==========")
print(decomposicao)
