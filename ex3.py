import random
numero_secreto = random.randint(1, 100)

tentativa = 1

while tentativa <= 20:
    palpite = int(input("Adivinhe o número secrero: "))
    if palpite == numero_secreto:
        print("Parábens, você acertou!")
        break
    
    else:
        if palpite > numero_secreto:
         print(" tente novamente")
        else:
         print("tente novamente")

        tentativa += 1

if tentativa > 20:
    print("Suas tentativas acabaram. O número secreto era", numero_secreto)
