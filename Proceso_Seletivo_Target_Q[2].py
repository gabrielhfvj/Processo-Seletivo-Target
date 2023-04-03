import json
import statistics as sts

data = open('dados.json')
dados_faturamento = json.load(data)

# print(dados_faturamento)
# Códigos para a leitura do arquivo '.json'.

faturamento_mensal = []
# Cria uma lista para armazenar todos os dias que houve faturamento.

for i in range(0, len(dados_faturamento)):
    # Percorre o faturamento diários de todos os 30 dias.
    faturamento_do_dia = dados_faturamento[i]['valor']

    if faturamento_do_dia > 0:
        faturamento_mensal.append(faturamento_do_dia)
    # Adiciona a lista de faturamento mensal o valor do faturamento diário dos dias em que houve faturamento.

faturamento_medio = sts.mean(faturamento_mensal)
faturamento_min = min(faturamento_mensal)
faturamento_max = max(faturamento_mensal)
# Funções para calcular a média, o menor e o maior valor referentes ao faturamento.

contador = 0
# Contador de dias para o loop que irá contar quantos dias o faturamento diário foi maior que o mensal.

for i in range(0, len(dados_faturamento)):
    faturamento_do_dia = dados_faturamento[i]['valor']

    if faturamento_do_dia > faturamento_medio:
        contador += 1


print(faturamento_medio)
print(
    f'O menor valor de faturamento ocorrido em um dia do mês foi de R${faturamento_min:.2f}.')
print(
    f'O maior valor de faturamento ocorrido em um dia do mês foi de R${faturamento_max:.2f}.')
print(
    f'O valor de faturamento diário foi superior à média mensal em {contador} dias.')

