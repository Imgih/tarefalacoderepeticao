
 #Faça um programa que simule a urna eletrônica.
#A tela a ser apresentada deverá ser da seguinte forma:
#1. Candidato Jair Rodrigues
#2. Candidato Carlos Luz
#3. Candidato Neves Rocha
#4. Nulo
#5. Branco
#Entre com o seu voto:
#O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes informações:
#a) O número de votos de cada candidato;
#b) A porcentagem de votos nulos;
#c) A porcentagem de votos brancos;
#d) O candidato vencedor.





Candidato_Jair_Rodrigues = 0
Candidato_Carlos_Luz = 0
Candidato_Neves_Rocha = 0
Nulo = 0
Branco = 0
total_votos = 0


while True: #informções dos votos
    print("\nAs opções são:\n 1-Candidato Jair Rodrigues\n 2- Candidato Carlos Luz\n 3-Candidato Neves Rocha\n 4-Nulo\n 5-Branco\n 6-Fim\n")
    print("\nEntre com o seu voto:")
    
   
    voto = input()
    
        #valida os votos
    if voto == '1':
        Candidato_Jair_Rodrigues += 1
        
    elif voto == '2':
        Candidato_Carlos_Luz += 1
        
    elif voto == '3':
        Candidato_Neves_Rocha += 1
        
    elif voto == '4':
        Nulo += 1
        
    elif voto == '5':
        Branco += 1
        
    elif voto == '6':
        break
    else:
        print("Voto invalido! Tente novamente.")
        continue
    
    
    total_votos += 1

# Calcula as porcentagens de votos nulos e brancos
percentual_nulos = Nulo / total_votos * 100
percentual_brancos = Branco / total_votos * 100

# Calcula o número total de votos de cada candidato
total_jair_rodrigues = Candidato_Jair_Rodrigues  / total_votos * 100
total_carlos_luz = Candidato_Carlos_Luz / total_votos * 100
total_neves_rocha = Candidato_Neves_Rocha / total_votos * 100

#Calculos dos resultados
if Candidato_Jair_Rodrigues > Candidato_Carlos_Luz and Candidato_Jair_Rodrigues > Candidato_Neves_Rocha:
    vencedor = " Candidato Jair Rodrigues"
    
elif Candidato_Carlos_Luz > Candidato_Jair_Rodrigues and Candidato_Carlos_Luz> Candidato_Neves_Rocha:
    vencedor = "Candidato Carlos Luz"
    
elif Candidato_Neves_Rocha > Candidato_Jair_Rodrigues and Candidato_Neves_Rocha > Candidato_Carlos_Luz:
    vencedor = "Candidato Neves Rocha"
else:
    vencedor = "Empate"
    




# IMostra os resultados
print("Número de votos para o Jair Rodrigues:", Candidato_Jair_Rodrigues)
print("Número de votos para o Carlos Luz:", Candidato_Carlos_Luz)
print("Número de votos para o Neves Rocha:", Candidato_Neves_Rocha)
print("Percentual de votos nulos:", percentual_nulos, "%")
print("Percentual de votos brancos:", percentual_brancos, "%")

print("Candidato vencedor:", vencedor)
if vencedor == "Empate":
    print("Haverá um segundo turno")

    