frase = str(input('Insira sua frase: '))
# A frase será inserida pelo usuário.

numero_de_caracteres = len(frase)
# Usa a função "len" para contar quantos caracteres estão presentes na frase.

for i in range(numero_de_caracteres-1, -1, -1):
    # Loop que percorre todos os caracteres da frase inserida, começando pelo último e seguindo até o primeiro.
    # Subtraímos 1 do "numero_de_carcteres" por questão de sintaxe do Python, caso nao o fizesse teríamos um erro de índice.
    
    print(frase[i], end='')
    # Usamos o paramêtro "end=''" para evitarmos a quebra de linha entre os prints.
