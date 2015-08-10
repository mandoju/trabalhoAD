
# -*- coding: latin-1 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline


#parametros
lambda_entrada = 0.5    ##lambda do problema
#numero_de_aleatorios = 10000 ##representa o número de variáveis aleatórias que irá ser gerado
tempo_simulacao = 1000
numero_ciclos= 1

##TODO: melhores nomes para as variáveis

media=0
tempo_entre_saida_final =  np.array([0] * 100)
for q in range(numero_ciclos):
    fila = 0
    i = 0
    j = 0
    servidor = 0
    tempo_proximo = 0
    entrada = 0  ##tempo até a próxima entrada
    tempo_proximo = 0  ##tempo até terminar a execução no servidor
    ##variáveis para calcular a média
    tempo = 0
    esperanca = 0
    fim = 0

    tempo_entre_saida =  []

    total_saido = 0
    stasis = 0


    while (1):

        #if(i == numero_de_aleatorios and j == numero_de_aleatorios):
            #esperanca = esperanca / tempo
            #print('a número médio de pessoas no sistema é: ' + str(esperanca))
            #media= media + esperanca/numero_ciclos
            ##tempo_entre_saida[:] = [x / total_saido for x in tempo_entre_saida]
            ##print('o tempo entre saida é:')
            ##print(tempo_entre_saida)
            ##tempo_entre_saida_final = map(add,tempo_entre_saida_final,tempo_entre_saida)
            ##tempo_entre_saida_final = tempo_entre_saida_final + np.array(tempo_entre_saida)
            ##tempo_entre_saida_final = [(x)/numero_ciclos for x in tempo_entre_saida]
        #    break
        if(tempo == tempo_simulacao):
            esperanca = esperanca / tempo
            #print('a número médio de pessoas no sistema é: ' + str(esperanca))
            media= media + esperanca/numero_ciclos
            break



        while(entrada == 0):
            entrada = int(np.random.exponential(1/lambda_entrada)) ##Gera uma nova entrada exponencial
            fila+= 1
            i += 1

        entrada -= 1

        ## while nescessário caso caia em um tempo = 0 novamente
        while(tempo_proximo == 0 and fila > 0):
            servidor = 1
            fila -= 1
            ##aqui vamos colocar na lista o tempo que vai demorar
            total_saido += 1

            exponencial = np.random.exponential(1)
            tempo_proximo = int(exponencial) ##Gera um novo tempo exponencial
            tempo_entre_saida.append(stasis + exponencial)
            stasis = 0

            j += 1
        if(fila == 0 and tempo_proximo == 0):
                ##aqui vamos contar o tempo da pessoa que saiu
                stasis +=1
                servidor = 0
        else:
                tempo_proximo -= 1

        ##coisas inuteis para parar quando já tudo processado
        ##nunca será executável pois para depois da ultima remessa da entrada


        esperanca += fila + servidor ##soma o número de clientes no sistema
        tempo += 1  ##adiciona mais um no tempo

##executando a função main
divisao_ciclos = np.array([numero_ciclos] * 100)

#print(tempo_entre_saida)
total = len(tempo_entre_saida)
#print(total)
#y_temp = np.array(range(total))
y = np.array(range(total))/total
tempo_entre_saida.sort()

plt.figure(figsize=(8, 6), dpi=100)

x_smooth = np.linspace(min(tempo_entre_saida), max(tempo_entre_saida), 1000)
y_smooth = spline (tempo_entre_saida, y, x_smooth)
plt.plot(x_smooth, y_smooth,'-', label="Curva Amortizada")
#plt.plot(xp, yp, 'bo', label="Pontos Da Curva")

plt.axis([0, 1.1*(max(tempo_entre_saida)), 0, 1.2*(max(y))])
plt.suptitle('Poisson1', fontsize=20)
plt.xlabel('tempo_entre_saidas', fontsize=15)
plt.ylabel('Y', fontsize=15)
plt.legend(loc=1, prop={'size':10})
plt.show()
