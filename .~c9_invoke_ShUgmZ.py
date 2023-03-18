totais = [0,0,0,0,0]
candidatos = ["Candidato Jair Rodrigues", "Candidato Carlos Luz", "Candidato Nevs Rocha", "Nulo", "Branco"]

print("1 - Candidato Jair Rodrigues\n", "2- Candidato Carlos Luz\n", "3-Candidato Nevs Rocha\n", "4- Nulo\n", "5-Branco\n", "6- Fim")
voto = int(input('Digite o número do Candidato:'))
while voto != 6:
    totais[voto-1] += 1                              #voto -1 serve para compatibilizar a posição do candidato na lista
    print('1 - Candidato A \n2 - Candidato B\n3 - Candidato C\n4 - Candidato D\n')
    voto = int(input('Digite o número do Candidato:'))

totalvotos = sum(totais)                             # função sum(lista) soma os valores dos itens da lista
vencedor = max(totais)                               # função max(lista) retorna o maior valor da lista 

for i in range(len(totais)):
    perc = totais[i]/totalvotos * 100
    print('\nVoto: {0}\nvotos: {1}\nPercentual:{2:.2f}%'.format(candidatos[i],totais[i], perc))
    if vencedor == totais[i]:
        v = i

print('\n\nO ', candidatos[v], ' foi eleito PRESIDENTE')