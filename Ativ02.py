class CalculoMedia(object):
    print("######## Segundo exercicio MÉDIA ########")

    nota1 = float(input("Digita sua primeira nota: "))
    nota2 = float(input("Digita sua segunda nota: "))
    nota3 = float(input ("Digita sua terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
   # print("A média de suas notas", nota1, nota2, nota3,"é está: ",media, sep=',')
    print("A média de suas notas", nota1, nota2,nota3, sep=', ')
    print ("é está: ", media)