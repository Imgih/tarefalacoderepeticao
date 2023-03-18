#1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido

tabuada = int(input("Tabuada do número (1 a 10): "))


for count in range(10):
    if tabuada > 0:
        print("%d * %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
    else:
        print("Não foi possível realizar")

