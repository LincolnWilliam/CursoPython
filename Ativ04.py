v_branco = float(input('Digite a quantidade de votos em branco: '))
v_nulos = float(input('Digite a quantidade de votos nuloes: '))
v_validos = float(input('Digite a quantidade de votos Validos: '))
total_votos = v_branco + v_nulos + v_validos

porcentagem_brancos = (v_branco / total_votos) * 100
porcentagem_nulos = (v_nulos / total_votos) * 100
porcentagem_validos = (v_validos / total_votos) * 100

print('Total de votos da eleição: ', total_votos)
print("porcentagem de votos em branco é {0:.2f} %".format(porcentagem_brancos))
print("porcentagem de votos Nulos é {0:.2f}%".format(porcentagem_nulos) )
print("porcentagem de votos Validos é {0:.2f} %".format(porcentagem_validos) )