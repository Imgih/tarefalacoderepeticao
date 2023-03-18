import random

numero_jogadas = int(input("Digite quntas vezes você quer jogar a moeda: "))

cara = 0
coroa =0

for i in range(numero_jogadas):
    resultado = random.randint(0, 1)
    if resultado == 0:
        print("Cara")
        cara += 1
    else:
        print("Coroa")
        coroa += 1
        
print(f"Total de caras: {cara}")
print(f"Total de coroas: {coroa}")

