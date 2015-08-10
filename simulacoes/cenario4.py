# -*- coding: latin-1 -*-
__author__ = 'Rodrigo'

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


def simula4():

    #parametros
    numero_ciclos= 1
    tempo_simulacao = 1000000
    u=[]#lista para plotar
    valor=[]#lista para plotar

    ##TODO: melhores nomes para as vari�veis

    for w in range(1,20):
        u_servidor = round(0.5*(w+1), 2)#lambda do problema
        media=0
        for q in range(numero_ciclos):
            lambda_entrada = 0.01  ##lambda fixo
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
            print(q)
            while (1):

                if(tempo == tempo_simulacao):
                    esperanca = esperanca / tempo
                    #print('a n�mero m�dio de pessoas no sistema �: ' + str(esperanca))
                    media= media + esperanca/numero_ciclos
                    break

                while(entrada == 0):
                    entrada = int(np.random.exponential(1/lambda_entrada)) ##Gera uma nova entrada exponencial
                    fila+= 1
                    i += 1

                entrada -= 1

                ## while nescess�rio caso caia em um tempo = 0 novamente
                resto = 0


                while(tempo_proximo == 0 and fila > 0):
                    servidor = 1
                    fila -= 1
                    aleatorio = np.random.random_sample()
                    if(aleatorio > 0.1):
                        fila +=1
                    exponencial = np.random.exponential(1/u_servidor)
                    tempo_proximo = int(exponencial)
                    resto += exponencial - tempo_proximo
                    if(resto > 1):
                        tempo_proximo += 1
                    j += 1
                if(fila == 0 and tempo_proximo == 0):
                        servidor = 0
                else:
                        tempo_proximo -= 1
                ##coisas inuteis para parar quando j� tudo processado
                ##nunca ser� execut�vel pois para depois da ultima remessa da entrada
                esperanca += fila + servidor ##soma o n�mero de clientes no sistema
                tempo += 1  ##adiciona mais um no tempo

        ##executando a fun��o main
        print("Media das medias: ", media)
        u.append(u_servidor)
        valor.append(media)

    plt.figure(figsize=(8, 6), dpi=100)
    x_smooth = np.linspace(min(u), max(u), 10000)
    y_smooth = spline (u, valor, x_smooth)
    plt.plot(x_smooth,y_smooth,'-b', label="Curva Amortizada")
    plt.plot(u, valor, 'bo', label="Pontos Da Curva")
    #plt.plot(lamb, valor2, '-ro', label="Curva Teste")
    plt.axis([0, 1.1*(max(u)), 0, 1.2*(max(valor))])
    plt.suptitle('Cen�rio-3', fontsize=20)
    plt.xlabel('Lambda', fontsize=15)
    plt.ylabel('M�dia', fontsize=15)
    plt.legend(loc=1, prop={'size':10})
    plt.show()
