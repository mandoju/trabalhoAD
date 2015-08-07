# -*- coding: latin-1 -*-
__author__ = 'jorge'
import numpy as np
import cenarios_reentrada as cn
from operator import add

def poisson1():


    #parametros
    lambda_entrada = 0.5    ##lambda do problema
    numero_de_aleatorios = 100 ##representa o número de variáveis aleatórias que irá ser gerado
    numero_ciclos= 10000

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

        tempo_entre_saida_atual = 0
        tempo_entre_saida =  [0] * 100

        total_saido = 0

        while (1):

            if(i == numero_de_aleatorios and j == numero_de_aleatorios):
                #esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                #media= media + esperanca/numero_ciclos
                tempo_entre_saida[:] = [x / total_saido for x in tempo_entre_saida]
                ##print('o tempo entre saida é:')
                ##print(tempo_entre_saida)
                ##tempo_entre_saida_final = map(add,tempo_entre_saida_final,tempo_entre_saida)
                tempo_entre_saida_final = tempo_entre_saida_final + np.array(tempo_entre_saida)
                ##tempo_entre_saida_final = [(x)/numero_ciclos for x in tempo_entre_saida]
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

                ##aqui vamos colocar na lista que somou + 1
                tempo_entre_saida[tempo_entre_saida_atual] += 1
                tempo_entre_saida_atual = 0
                total_saido += 1

                tempo_proximo = int(np.random.exponential(1)) ##Gera um novo tempo exponencial
                j += 1
            if(fila == 0 and tempo_proximo == 0):
                    ##aqui vamos contar o tempo da pessoa que saiu
                    tempo_entre_saida[tempo_entre_saida_atual] += 1
                    tempo_entre_saida_atual = 0
                    total_saido += 1
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

            tempo_entre_saida_atual += 1
            esperanca += fila + servidor ##soma o número de clientes no sistema
            tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    divisao_ciclos = np.array([numero_ciclos] * 100)
    ##tempo_entre_saida_final = [(x)/numero_ciclos for x in tempo_entre_saida]
    tempo_entre_saida_final = np.divide(tempo_entre_saida_final,divisao_ciclos)
    print(tempo_entre_saida_final)


##TODO: ESTA FUNÇÃO NÃO ESTÁ IMPLEMENTADA
def poisson2():
   #parametros
    u_servidor = 1    ##U do servidor (tem que variar 1,1,5,2...10
    numero_ciclos= 1
    tempo_simulacao = 1000000

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
        tempo_proximo = 0  ##tempo até terminar a execução no servidor
        ##variáveis para calcular a média
        tempo = 0
        esperanca = 0
        fim = 0
        print(q)
        while (1):

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
            ##coisas inuteis para parar quando já tudo processado
            ##nunca será executável pois para depois da ultima remessa da entrada
            esperanca += fila + servidor ##soma o número de clientes no sistema
            tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    print("Media das medias: ", media)
