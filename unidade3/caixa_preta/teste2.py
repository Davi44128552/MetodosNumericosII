from householder import *
from qr import *
from caixa_preta import *

A = np.array([[2, 1, 1],
              [4, -6, 0],
              [-2, 7, 2]])
n = A.shape[0]

lamb, V = caixa_preta(A)

# Resultados
print("Autovalores:")
print(lamb)

print("\nAutovetores:")
print(V)
