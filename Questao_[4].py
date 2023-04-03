faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53
# Valores de faturamento mensal de uma distribuidora, detalhados por estado.

faturamento_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros
# Faturamento tolta somando o faturamento de todos os estados.

percentual_sp = (faturamento_sp / faturamento_total) * 100
percentual_rj = (faturamento_rj / faturamento_total) * 100
percentual_mg = (faturamento_mg / faturamento_total) * 100
percentual_es = (faturamento_es / faturamento_total) * 100
percentual_outros = (faturamento_outros / faturamento_total) * 100
# Calcula a fração de cada estado em relação ao faturamento total, e transforma em um valor percentual.

print(f'O percentual de representação do estado de SP em relação ao valor total mensal da distribuidora é: {percentual_sp:.2f}%')
print(f'O percentual de representação do estado de RJ em relação ao valor total mensal da distribuidora é: {percentual_rj:.2f}%')
print(f'O percentual de representação do estado de MG em relação ao valor total mensal da distribuidora é: {percentual_mg:.2f}%')
print(f'O percentual de representação do estado de ES em relação ao valor total mensal da distribuidora é: {percentual_es:.2f}%')
print(f'O percentual de representação dos Outros Estados em relação ao valor total mensal da distribuidora é: {percentual_outros:.2f}%')
