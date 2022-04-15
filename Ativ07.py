# O custo de um carro novo ao consumidor é a soma do custo de
# fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um
# algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

custo = float(input('Digite o custo do carro R$ '))
percentualDistribuidor = custo * (28/100)
impostos = custo * (45/100)

custoFinal = custo + percentualDistribuidor + impostos

print(f'Custo final de um carro é: {custoFinal:.3f}')
'''
custo_carro = ? 
percentual_Distribuidor = 28%
impostos_custofabrica = 45%
custofinal = custo_carro + percentual_distribuidor + impostos_custofabrica
'''