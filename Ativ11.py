'''
A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que
são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25.
Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades,
se o índice crescer para 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades,
se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um algoritmo que leia o
índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas

'''
# grupo1 = 0,3 sao intimadas a suspender atividades
# grupo2 = 0,4 sao intimadas a suspender atividades
# grupo3 = 0,5 sao intimados a suspender atividades
# indice_polucicao = 0,05 até 0,25

indice = float(input('informe o indice de poluição: '))

if indice >= 0.5:
    print('Todos os grupos estão intimados a suspender suas atividades')

elif indice >= 0.4:
    print(f'Com indice de: {indice} \nEmpresas do Grupo 1° e Grupo 2° estão intimadas a suspender suas atividades')

elif indice >= 0.3:
    print(f'Com indice de: {indice} \nEmpresas do Grupo 1° estão intimadas a suspender suas atividades')

else:
    print (f'com indice: {indice} \nTodos os Grupos podem manter suas atividades ! ')