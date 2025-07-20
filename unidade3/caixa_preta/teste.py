from householder import *
from qr import *
from caixa_preta import *

# Primeira matriz resolvida em aula
A = np.array(
    [
        [21, 29, 21, 32, 40],
        [29, 94, 62, 87, 94],
        [21, 62, 131, 90, 73],
        [32, 87, 90, 94, 95],
        [40, 94, 73, 95, 105],
    ]
)
n = A.shape[0]

lamb, V = caixa_preta(A)

# Resultados
print("Autovalores:")
print(lamb)

print("\nAutovetores:")
print(V)
