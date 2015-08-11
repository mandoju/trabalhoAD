
# -*- coding: latin-1 -*-
__author__ = 'jorge'

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline


def simula_poisson4():
    print('poisson2')
   #parametros
    u_servidor = 1    ##U do servidor (tem que variar 1,1,5,2...10
    numero_ciclos= 1
    tempo_simulacao = 10000

    ##TODO: melhores nomes para as variáveis

    media=0
    for q in range(numero_ciclos):
        lambda_entrada = 0.01  ##lambda fixo
        fila = 0
        i = 0
        j = 0
        servidor = 0
        tempo_proximo = 0
        entrada = 0  ##tempo até a próxima entrada
        entrada_raw = 0
        tempo_proximo = 0  ##tempo até terminar a execução no servidor
        tempo_proximo_raw = 0
        ##variáveis para calcular a média
        tempo = 0
        esperanca = 0
        fim = 0

        tempo_entre_entrada =  []
        volta = 0

        total_saido = 0
        stasis = 0


        while (1):

            if(tempo == tempo_simulacao):
                esperanca = esperanca / tempo
                #tempo_entre_entrada.append(exponencial_entrada)
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break

            while(entrada == 0):
                exponencial_entrada = np.random.exponential(1/lambda_entrada)
                entrada = int(exponencial_entrada) ##Gera uma nova entrada exponencial

                entrada_raw = exponencial_entrada
                fila+= 1

                if(tempo_proximo_raw <= entrada_raw):
                        tempo_entre_entrada.append( entrada_raw - tempo_proximo_raw)

                i += 1

            entrada -= 1
            entrada_raw -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0


            while(tempo_proximo == 0 and fila > 0):
                servidor = 1
                exponencial_servico = np.random.exponential(1/u_servidor)
                tempo_proximo = int(exponencial_servico)
                tempo_proximo_raw = exponencial_servico
                resto += exponencial_servico - tempo_proximo

                if(volta == 0):
                    fila -=1

                aleatorio = np.random.random_sample()
                if(aleatorio > 0.1):
                    volta = 1
                    if(tempo_proximo_raw >= entrada_raw):
                        tempo_entre_entrada.append(tempo_proximo_raw - entrada_raw )
                    ##fila +=1
                else:
                    ##tempo_entre_saida.append(stasis + exponencial)
                    volta = 0




                stasis = 0


                if(resto > 1):
                    tempo_proximo += 1
                j += 1
            if(fila == 0 and tempo_proximo == 0):
                    stasis +=1
                    servidor = 0
            else:
                    tempo_proximo -= 1
                    tempo_proximo_raw -= 1
            ##coisas inuteis para parar quando já tudo processado
            ##nunca será executável pois para depois da ultima remessa da entrada
            esperanca += fila + servidor ##soma o número de clientes no sistema
            tempo += 1  ##adiciona mais um no tempo
    #print(tempo_entre_saida)
    total = len(tempo_entre_entrada)
    print(total)
    #y_temp = np.array(range(total))
    y = np.array(range(total))/total
    ##executando a função main
    #print("Media das medias: ", media)

    tempo_entre_entrada.sort()

    plt.figure(figsize=(8, 6), dpi=100)
    plt.plot(tempo_entre_entrada, y, 'bo', label="Pontos Da Curva")


    cdf_expo = []
    for tempo in tempo_entre_entrada:
        analitico = 1 - np.exp(-1*lambda_entrada*tempo)
        print(analitico)
        cdf_expo.append(analitico)
    plt.plot(tempo_entre_entrada, cdf_expo,'-r', label="Exponencial")

    plt.axis([0, 1.1*(max(tempo_entre_entrada)), 0, 1.2*(max(y))])
    plt.suptitle('Cenário 4 - Partidas exógenas', fontsize=20)
    plt.xlabel('Tempo entre saídas', fontsize=15)
    plt.ylabel('Y', fontsize=15)
    plt.legend(loc=1, prop={'size':10})
    plt.show()