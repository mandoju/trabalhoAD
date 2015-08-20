# -*- coding: latin-1 -*-
__author__ = 'jorge'
import numpy as np
import cenarios_reentrada as cn
import checar_saida as ch

import verificar_pasta as pasta
import academia as academia
from simulacoes import cenario1 as c1
from simulacoes import cenario2 as c2
from simulacoes import poisson2 as p2
from simulacoes import poisson3 as p3
from simulacoes import poisson4 as p4


def main():

    #parametros
    lambda_entrada = 0.51    ##lambda do problema
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
    lambda_entrada = 0.2   ##lambda do problema
    lambda_tempo = 1/lambda_entrada ##lambda para tempo
    print(lambda_tempo)
    numero_ciclos= 1000
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

            resto = 0
            while(entrada == 0):
                entrada = int(lambda_tempo) ##Gera uma nova entrada exponencial
                resto += lambda_tempo - int(lambda_tempo)
                if(resto > 1):
                    entrada += 1
                fila+= 1
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0
            while(tempo_proximo == 0 and fila > 0):
                servidor = 1
                fila -= 1
                tempo_proximo = int(np.random.exponential(1))
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
    print('oi')

    ##ALERTA!
    ##NESTE CASO SÓ ALTERA O U DO SERVIDOR
    ##1, 1.5,2,2.5,...,10

    #parametros
    u_servidor = 5.5  ##este parametro que irá variar
    numero_ciclos= 1000
    tempo_simulacao= 1000 ##número de loops do while

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

            resto = 0
            while(entrada == 0):
                uniforme = np.random.uniform(5,15)
                entrada = int(uniforme) ##Gera uma nova entrada exponencial
                resto += uniforme - entrada
                if(resto > 1):
                    entrada += 1
                fila+= 1
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0
            while(tempo_proximo == 0 and fila > 0):
                servidor = 1
                fila -= 1
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
##deterministico()
##executando uniforme
##uniforme()
##cn.cenario4()
##ch.poisson1()
##c1.poisson1()
##main()
##ch.poisson2()
##pasta.pasta1()
##p4.simula_poisson4()
##academia.academia_cliente()
##c2.simula2()
##ch.poisson2()
pasta.pasta2_correto()