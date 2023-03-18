#6 - Faça um algoritmo em python capaz de realizar o cálculo de rentabilidade de uma poupança,
#esse algoritmo deve receber como entrada o valor inicial que o usuário está disposto a guardar.
#Como saída, o programa deve imprimir na tela mês a mês o montante por 12 meses
#aplicado a uma taxa de 0,5 % ao mês de rentabilidade.#

#A fórmula do montante (M) de uma aplicação financeira é dada por:

#M = P * (1 + i)^n

#onde:

#P é o capital inicial (ou principal)
#i é a taxa de juros aplicada (em forma decimal) - divida o valor dado por 100
#n é o número de períodos de tempo em que o dinheiro ficará investido.



capital_inicial = float(input('Digite o depósito inicial: R$  ' )) 
i = float(input('Agora, digite a taxa de juros de uma poupança: ')) #digite o valor em porcentagem
i = (i/100) #conversão de porcentagem para decimal
t = 1
vf = 0

print('*' * 18) 

while(t <= 12): #12 meses de calculos
    vf = capital_inicial * (1 + i) ** t # formula do juros compostos
    t = t + 1 # meses 
    print(f'\nNo mês {t}, o valor dos monate será igual a R$'"{0:.2f}".format(round(vf,2))) #12 meses se iniciando a partir do mês 2 com arrendodamento de duas casas
  

   

