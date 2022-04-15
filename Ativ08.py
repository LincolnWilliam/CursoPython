# maior idade , valorIngresso 50,00 reais.

idade = int(input("Digite sua idade: "))
valorIngresso = 50.0
meiaEntrada = valorIngresso /2

if idade >= 18:
    print(f"Valor da sua entrada é :{valorIngresso:.2f}")
else:
    print(f"Meia entrada , valor do ingresso é:{meiaEntrada:.2f}")
