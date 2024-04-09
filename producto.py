import numpy as np
"""
vector_1 = np.array([1,9,6])
vector_2 = np.array([1,4,6])

vector = vector_1.dot(vector_2)
print(vector)
"""
"""
# Matriz 2x2
f = np.eye(2)
# Matriz 2x2 con solo numeros 7 (siete)
e = np.full((2,2),7)
print(f)
print(e)
# Probar la longitud de las matrices
print(f.shape, e.shape)

# Calcular el producto de las dos matrices 
h = e.dot(f)
print(h)

"""
"""
m = np.array([(2,4,6),(2,6,8)])
n = np.array([(3,8),(3,6),(2,4)])

print(m)
print()
print(n)

print(m.shape, n.shape)

u = m.dot(n)
print(u)
"""

matriz_a = np.random.random((100,50))
matriz_b = np.random.random((50,30))

print(matriz_a.shape, matriz_b.shape)

resultado = matriz_a.dot(matriz_b)
print(resultado)

print(resultado.shape)