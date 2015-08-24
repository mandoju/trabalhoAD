__author__ = 'jorge'
# -*- coding: latin-1 -*-
__author__ = 'jorge'

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


def academia_utilizacao():
    ##ALERTA!
    ##NESTE CASO SÓ ALTERA O U DO SERVIDOR
    ##1, 1.5,2,2.5,...,10

    #parametros



    lambda_entrada = 0.1
    u_esteira = 5  ##este parametro que irá variar
    u_bike = 5
    p = 1
    q = 0.9 ##considera isso como q

    numero_ciclos= 100
    tempo_simulacao= 1000 ##número de loops do while

    ##TODO: melhores nomes para as variáveis

    media_esteira=0
    media_bicicleta=0
    for k in range(numero_ciclos):
        print('ciclo:' + str(k))
        fila_esteira = 0
        fila_bicicleta = 0
        i = 0
        j = 0
        servidor_esteira = 0
        servidor_bicicleta = 0
        utilizacao_esteira = 0
        utilizacao_bicicleta = 0
        entrada = 0  ##tempo até a próxima entrada
        tempo_proximo_esteira = 0  ##tempo até terminar a execução no servidor
        tempo_proximo_bicicleta = 0
        ##variáveis para calcular a média
        tempo = 0
        esperanca = 0
        fim = 0

        while (1):

            if(tempo >= tempo_simulacao):
                utilizacao_esteira = utilizacao_esteira / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media_esteira = media_esteira + utilizacao_esteira/numero_ciclos
                utilizacao_bicicleta = utilizacao_bicicleta / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media_bicicleta = media_bicicleta + utilizacao_bicicleta/numero_ciclos
                break
            ##if(i == numero_de_aleatorios and j == numero_de_aleatorios):
            ##    esperanca = esperanca / tempo
            ##    #print('a número médio de pessoas no sistema é: ' + str(esperanca))
            ##    media= media + esperanca/numero_ciclos
            ##    break

            resto = 0
            while(entrada == 0):
                exponencial = np.random.exponential(lambda_entrada)
                entrada = exponencial ##Gera uma nova entrada exponencial
                fila_esteira += 1
                i += 1


            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0
            while(tempo_proximo_esteira == 0 and fila_esteira > 0):
                servidor_esteira = 1
                fila_esteira -= 1
                aleatorio = np.random.random_sample()
                if(aleatorio <= p):
                    fila_bicicleta +=1
                exponencial = np.random.exponential(1/u_esteira)
                tempo_proximo_esteira = exponencial
                j += 1


            if(fila_esteira == 0 and tempo_proximo_esteira == 0):
                    servidor_esteira = 0


            while(tempo_proximo_bicicleta == 0 and fila_bicicleta > 0):
                servidor_bicicleta = 1
                fila_bicicleta -= 1
                aleatorio = np.random.random_sample()
                if(aleatorio <= q):
                    fila_esteira += 1
                exponencial = np.random.exponential(1/u_bike)
                tempo_proximo_bicicleta = exponencial
                j += 1


            if(fila_bicicleta == 0 and tempo_proximo_bicicleta == 0):
                    servidor = 0


            #tempo_passado = min(entrada,tempo_proximo_esteira,tempo_proximo_bicicleta)
            a = np.array([entrada,tempo_proximo_esteira,tempo_proximo_bicicleta])
            tempo_passado = np.min(a[np.nonzero(a)])

            #print('tempo entrada:' + str(entrada) + ' | tempo_proximo_esteira:' + str(tempo_proximo_esteira) + ' | tempo proximo_bicicleta' + str(tempo_proximo_bicicleta) + ' | tempo_passado:' + str(tempo_passado))

            entrada -= tempo_passado
            if(tempo_proximo_esteira != 0):
                tempo_proximo_esteira -= tempo_passado
                utilizacao_esteira += tempo_passado
            if(tempo_proximo_bicicleta != 0):
                tempo_proximo_bicicleta -= tempo_passado
                utilizacao_bicicleta += tempo_passado
            tempo += tempo_passado
            ##print(tempo)



            ##print('tempo_proximo_esteira:' + str(fila_esteira))

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
        print(utilizacao_bicicleta)
        print(utilizacao_esteira)
            ##esperanca += fila + servidor ##soma o número de clientes no sistema
            ##tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    print("Media das medias esteira: ", media_esteira)
    print("Media das medias bicicleta: ", media_bicicleta)
