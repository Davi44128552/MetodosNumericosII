from householder import *
from qr import *

# Suponha A simétrica
A = np.array([
    [3.0, 1.0],
    [1.0, 2.0]
])
n = A.shape[0]

# 1. Tridiagonalização
A_tridiag, H = tridiagonal_householder(A)

# 2. Método QR para encontrar autovalores e autovetores de A_tridiag
P_qr, lamb = qr(A_tridiag)

# 3. Autovetores reais de A
V = H @ P_qr

# Resultados
print("Autovalores:")
print(np.round(lamb, 6))

print("\nAutovetores (colunas de V):")
print(np.round(V, 6))

# Verificação: A @ V ≈ V @ diag(lamb)
print("\nA @ V:")
print(np.round(A @ V, 6))

print("\nV @ diag(lamb):")
print(np.round(V @ np.diag(lamb), 6))
