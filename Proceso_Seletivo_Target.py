# A entrada do número será feita aleatoriamente usando o comando "randint", da biblioteca "Random".

import random as rnd

number = rnd.randint(0, 10000)


# Algoritmo que irá calcular a sequência de Fibonacci.

f_1 = 0
f_2 = 1
# 2 primeiros termos da sequência de Fibonacci.

while True:
    # Cálcula a sequência de Fibonacci até o código mandá-lo parar.

    if number == f_1 or number == f_2:
        print(f'Número = {number}')
        print(
            f'O número aleatorizado faz parte de sequência de Fibonacci!')
        break
    # Checa se o número aleatorizado é o primero ou o segundo termo da sequência de Fibonacci.

    f_3 = f_1 + f_2
    f_1 = f_2
    f_2 = f_3
    # Código para movimentar-se na sequência de termo em termo, sempre à direita, começando pelo terceiro termo.

    if f_3 == number:
        print(f'Número = {number}')
        print(
            f'O número aleatorizado faz parte de sequência de Fibonacci!')
        break
    # Checa se o número aleatorizado é igual ao n-ésimo termo da sequência de Fibonacci, começando pelo terceiro.

    if f_3 > number:
        print(f'Número = {number}')
        print(
            f'O número aleatorizado NÃO faz parte de sequência de Fibonacci!')
        break
    # A partir do momento que o n-ésimo termo da sequência ultrapassa o número aleatorizado, é impossível que eles sejam iguais.
