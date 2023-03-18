#7 - Faça um programa que mostre o fatorial de um número fornecido pelo usuário.


numero = int(input("Fatorial de: "))

result = 1
count = 1

while count <= numero:
    result   *= count
    count += 1
print("{0:.2f}".format(round(result,2)))