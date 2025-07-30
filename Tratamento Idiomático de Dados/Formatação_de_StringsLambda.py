# f-strings (Python 3.6+)
nome = "João"
idade = 30
print(f"Olá {nome}, você tem {idade} anos")

# Formatação com expressões
import math
radius = 5
print(f"Área do círculo: {math.pi * radius**2:.2f}")

# Lambda functions
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Quadrados
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados[:5])  # [1, 4, 9, 16, 25]

# Ordenação personalizada
pessoas = [('Ana', 25), ('João', 30), ('Maria', 20)]
pessoas.sort(key=lambda pessoa: pessoa[1])  # Ordenar por idade
print(pessoas)  # [('Maria', 20), ('Ana', 25), ('João', 30)]