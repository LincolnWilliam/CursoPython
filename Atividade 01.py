print("########## Primeiro exercicio Calculo IMC #########")
class CalculoImc (object):
 peso = float(input ('digite o peso: '))
 altura = float(input ('digite a altura: '))

 imc = peso / altura ** 2

 print (f"O seu IMC é:  ",imc)

 if imc < 16:
     print('Magreza grave')

 elif imc < 17:
     print('Magreza moderada')

 elif imc < 18:
     print('Magreza leve')

 elif imc < 25:
     print('Magreza grave')

 elif imc < 30:
     print('Sobrepeso')

 elif imc < 35:
     print('Obsedidade em Grau I')
