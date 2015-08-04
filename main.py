# -*- coding: latin-1 -*-
__author__ = 'jorge'
import numpy as np
def main():


    #parametros
    lambda_entrada = 0.05    ##lambda do problema
    numero_de_aleatorios = 100 ##representa o número de variáveis aleatórias que irá ser gerado
    numero_ciclos= 10000

    ##TODO: melhores nomes para as variáveis

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

            if(i == numero_de_aleatorios and j == numero_de_aleatorios):
                esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break

            while(entrada == 0 and i < numero_de_aleatorios):
                entrada = int(np.random.exponential(1/lambda_entrada)) ##Gera uma nova entrada exponencial
                fila+= 1
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            while(tempo_proximo == 0 and fila > 0 and j < numero_de_aleatorios):
                servidor = 1
                fila -= 1
                tempo_proximo = int(np.random.exponential(1)) ##Gera um novo tempo exponencial
                j += 1
            if(fila == 0 and tempo_proximo == 0):
                    servidor = 0
            else:
                    tempo_proximo -= 1

            ##coisas inuteis para parar quando já tudo processado
            ##nunca será executável pois para depois da ultima remessa da entrada
            if(fim == 0):
                ##print('fila = ' + str(fila))
                ##print('servidor = ' + str(servidor))
                pass
            else:
                return
            if(not(fila > 0 or ( i < numero_de_aleatorios and j < numero_de_aleatorios))):
                fim = 1

            esperanca += fila + servidor ##soma o número de clientes no sistema
            tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    print("Media das medias: ", media)


def deterministico():


    #parametros
    lambda_entrada = 0.95    ##lambda do problema
    lambda_tempo = 1/lambda_entrada ##lambda para tempo
    numero_de_aleatorios = 100 ##representa o número de variáveis aleatórias que irá ser gerado
    numero_ciclos= 10000
    tempo_simulacao = 1000  ##número de loops do while

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


            if(tempo == tempo_simulacao):
                esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break
            ##if(i == numero_de_aleatorios and j == numero_de_aleatorios):
            ##    esperanca = esperanca / tempo
            ##    #print('a número médio de pessoas no sistema é: ' + str(esperanca))
            ##    media= media + esperanca/numero_ciclos
            ##    break

            while(entrada == 0 and i < numero_de_aleatorios):
                entrada = int(lambda_tempo) ##Gera uma nova entrada exponencial
                fila+= 1
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0
            while(tempo_proximo == 0 and fila > 0 and j < numero_de_aleatorios):
                servidor = 1
                fila -= 1
                tempo_proximo = int(1)
                j += 1
            if(fila == 0 and tempo_proximo == 0):
                    servidor = 0
            else:
                    tempo_proximo -= 1

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
    print("Media das medias: ", media)


def uniforme():


    ##ALERTA!
    ##NESTE CASO SÓ ALTERA O U DO SERVIDOR
    ##1, 1.5,2,2.5,...,10

    #parametros
    u_servidor = 1  ##este parametro que irá variar
    numero_de_aleatorios = 100 ##representa o número de variáveis aleatórias que irá ser gerado
    numero_ciclos= 10000
    tempo_simulacao= 10000 ##número de loops do while

    ##TODO: melhores nomes para as variáveis

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

            if(tempo == tempo_simulacao):
                esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break
            ##if(i == numero_de_aleatorios and j == numero_de_aleatorios):
            ##    esperanca = esperanca / tempo
            ##    #print('a número médio de pessoas no sistema é: ' + str(esperanca))
            ##    media= media + esperanca/numero_ciclos
            ##    break

            while(entrada == 0 and i < numero_de_aleatorios):
                entrada = int(np.random.uniform(5,15)) ##Gera uma nova entrada exponencial
                fila+= 1
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0
            while(tempo_proximo == 0 and fila > 0 and j < numero_de_aleatorios):
                servidor = 1
                fila -= 1
                tempo_proximo = int(u_servidor)
                j += 1
            if(fila == 0 and tempo_proximo == 0):
                    servidor = 0
            else:
                    tempo_proximo -= 1

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
    print("Media das medias: ", media)



##executando a M/M/1
##main()
##executando a determinística
deterministico()