class CalculoArea(object):
    print("######## Terceiro exercicio ÁREA QUADRADO ########")

    lado = float(input("Digite o lado do quadrado: "))
    area = lado * lado
    print("A área do quadrado é: ",area)


class AreaTriangulo (object):
    print("######## Quarto exercicio ÁREA TRIANGULO ########")

    base = float(input("Digite a base do Triangulo: "))
    altura = float(input("Digite a altura do Triangulo: "))

    area = base * altura / 2

    print("Tendo o triangulo uma base de: ", base," e uma Altura de: ", altura, "sua área é de: ", area)