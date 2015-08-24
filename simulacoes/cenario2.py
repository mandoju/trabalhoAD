# -*- coding: latin-1 -*-
__author__ = 'Rodrigo'

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

def simula2():
    #parametros
    numero_ciclos= 1000
    tempo_simulacao = 1000  ##número de loops do while
    lamb=[]#lista para plotar
    valor=[]#lista para plotar

    for w in range(18):
        lambda_entrada = round(0.05*(w+1), 2)#lambda do problema
        lambda_tempo = 1/lambda_entrada ##lambda para tempo
        media=0

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

            while (1):

                if(tempo >= tempo_simulacao):
                    esperanca = esperanca / tempo
                    #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                    media= media + esperanca/numero_ciclos
                    break
                ##if(i == numero_de_aleatorios and j == numero_de_aleatorios):
                ##    esperanca = esperanca / tempo
                ##    #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                ##    media= media + esperanca/numero_ciclos
                ##    break

                resto = 0
                if(entrada == 0):
                    entrada = 1/lambda_tempo ##Gera uma nova entrada exponencial
                    fila+= 1
                    i += 1

                entrada -= 1

                ## while nescessário caso caia em um tempo = 0 novamente
                resto = 0
                if(tempo_proximo == 0 and fila > 0):
                    servidor = 1
                    fila -= 1
                    tempo_proximo = np.random.exponential(1)
                    j += 1
                if(fila == 0 and tempo_proximo == 0):
                        servidor = 0

                a = np.array([entrada,tempo_proximo])
                tempo_passado = np.min(a[np.nonzero(a)])

            #print('tempo entrada:' + str(entrada) + ' | tempo_proximo_esteira:' + str(tempo_proximo_esteira) + ' | tempo proximo_bicicleta' + str(tempo_proximo_bicicleta) + ' | tempo_passado:' + str(tempo_passado))

                entrada -= tempo_passado
                if(tempo_proximo != 0):
                    tempo_proximo -= tempo_passado
                tempo += tempo_passado
                ##print(tempo)

                ##coisas inuteis para parar quando já tudo processado
                ##nunca será executável pois para depois da ultima remessa da entrada
                if(fim == 0):
                    ##print('fila = ' + str(fila))
                    ##print('servidor = ' + str(servidor))
                    pass
                else:
                    break
                if(tempo == tempo_simulacao):
                    fim = 1

                esperanca += fila + servidor ##soma o número de clientes no sistema
                #esperanca += fila
                tempo += 1  ##adiciona mais um no tempo

        ##executando a função main
        print("Media das medias com lambda: ",lambda_entrada, media)
        lamb.append(lambda_entrada)
        valor.append(media)

    plt.figure(figsize=(8, 6), dpi=100)
    x_smooth = np.linspace(min(lamb), max(lamb), 10000)
    y_smooth = spline (lamb, valor, x_smooth)
    plt.plot(x_smooth,y_smooth,'-b', label="Curva Amortizada")
    plt.plot(lamb, valor, 'bo', label="Pontos Da Curva")
    #plt.plot(lamb, valor2, '-ro', label="Curva Teste")
    plt.axis([0, 1.1*(max(lamb)), 0, 1.2*(max(valor))])
    plt.suptitle('Cenário-2', fontsize=20)
    plt.xlabel('Lambda', fontsize=15)
    plt.ylabel('Média', fontsize=15)
    plt.legend(loc=1, prop={'size':10})
    plt.show()

