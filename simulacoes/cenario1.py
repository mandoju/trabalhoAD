    # -*- coding: latin-1 -*-
__author__ = 'Rodrigo'

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

def simula1():

    #parametros
    numero_de_aleatorios = 100 ##representa o n�mero de vari�veis aleat�rias que ir� ser gerado
    numero_ciclos= 10000 #numero de ciclos para tirar a media
    lamb=[]#lista para plotar
    valor=[]#lista para plotar

    ##TODO: melhores nomes para as vari�veis

    for w in range(18):
        lambda_entrada = round(0.05*(w+1), 2)#lambda do problema
        media=0

        for q in range(numero_ciclos):
            fila = 0
            i = 0
            j = 0
            servidor = 0
            tempo_proximo = 0
            entrada = 0  ##tempo at� a pr�xima entrada
            tempo_proximo = 0  ##tempo at� terminar a execu��o no servidor
            ##vari�veis para calcular a m�dia
            tempo = 0
            esperanca = 0
            fim = 0

            while (1):

                if(i == numero_de_aleatorios and j == numero_de_aleatorios):
                    esperanca = esperanca / tempo
                    #print('a n�mero m�dio de pessoas no sistema �: ' + str(esperanca))
                    media= media + esperanca/numero_ciclos
                    break

                while(entrada == 0 and i < numero_de_aleatorios):
                    entrada = int(np.random.exponential(1/lambda_entrada)) ##Gera uma nova entrada exponencial
                    fila+= 1
                    i += 1

                entrada -= 1

                ## while nescess�rio caso caia em um tempo = 0 novamente
                while(tempo_proximo == 0 and fila > 0 and j < numero_de_aleatorios):
                    servidor = 1
                    fila -= 1
                    tempo_proximo = int(np.random.exponential(1)) ##Gera um novo tempo exponencial
                    j += 1
                if(fila == 0 and tempo_proximo == 0):
                        servidor = 0
                else:
                        tempo_proximo -= 1

                ##coisas inuteis para parar quando j� tudo processado
                ##nunca ser� execut�vel pois para depois da ultima remessa da entrada
                if(fim == 0):
                    ##print('fila = ' + str(fila))
                    ##print('servidor = ' + str(servidor))
                    pass
                else:
                    return
                if(not(fila > 0 or ( i < numero_de_aleatorios and j < numero_de_aleatorios))):
                    fim = 1

                esperanca += fila + servidor ##soma o n�mero de clientes no sistema
                tempo += 1  ##adiciona mais um no tempo

        ##executando a fun��o main
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
    plt.suptitle('Cen�rio-1', fontsize=20)
    plt.xlabel('Lambda', fontsize=15)
    plt.ylabel('M�dia', fontsize=15)
    plt.legend(loc=1, prop={'size':10})
    plt.show()


