import random

secreto = random.randint(1,50)

valor = 0
while valor != secreto:
    valor = int(input('Ingrese un numero: '))

    if valor > secreto:
        print('Muy alto')
        continue

    if valor < secreto:
        print('Muy bajo')
        continue

print('Acertaste')    
