# -*- coding: latin-1 -*-
__author__ = 'Rodrigo'

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


def simula3():
    ##ALERTA!
    ##NESTE CASO SÓ ALTERA O U DO SERVIDOR
    ##1, 1.5,2,2.5,...,10

    #parametros
    #u_servidor = 1  ##este parametro que irá variar
    numero_ciclos= 1000
    tempo_simulacao= 10000 ##número de loops do while
    u=[]#lista para plotar
    valor=[]#lista para plotar

    ##TODO: melhores nomes para as variáveis

    for w in range(1,20):
        u_servidor = round(0.5*(w+1), 2)#lambda do problema
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
                    uniforme = np.random.uniform(5,15)
                    entrada = uniforme ##Gera uma nova entrada exponencial
                    fila+= 1
                    i += 1

                entrada -= 1

                ## while nescessário caso caia em um tempo = 0 novamente
                resto = 0
                if(tempo_proximo == 0 and fila > 0):
                    servidor = 1
                    fila -= 1
                    exponencial = np.random.exponential(1/u_servidor)
                    tempo_proximo = exponencial
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
                tempo += 1  ##adiciona mais um no tempo

        ##executando a função main
        print("Media das medias com U: ",u_servidor, media)
        u.append(u_servidor)
        valor.append(media)

    plt.figure(figsize=(8, 6), dpi=100)
    x_smooth = np.linspace(min(u), max(u), 10000)
    y_smooth = spline (u, valor, x_smooth)
    plt.plot(x_smooth,y_smooth,'-b', label="Curva Amortizada")
    plt.plot(u, valor, 'bo', label="Pontos Da Curva")
    #plt.plot(lamb, valor2, '-ro', label="Curva Teste")
    plt.axis([0, 1.1*(max(u)), 0, 1.2*(max(valor))])
    plt.suptitle('Cenário-3', fontsize=20)
    plt.xlabel('Lambda', fontsize=15)
    plt.ylabel('Média', fontsize=15)
    plt.legend(loc=1, prop={'size':10})
    plt.show()
