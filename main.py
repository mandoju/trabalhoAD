 # -*- coding: latin-1 -*-

__author__ = 'jorge'
import numpy as np
def main():


    #parametros
    lambda_entrada = 0.1    ##lambda do problema
    numero_de_aleatorios = 100 ##representa o número de variáveis aleatórias que irá ser gerado

    fila = 0
    i = 0
    j = 0
    servidor = 0
    tempo_proximo = 0

    ##variáveis para calcular a média
    tempo = 0
    esperanca = 0

    ##entrada_lista =  np.random.poisson(lambda_entrada,100)

    entrada_lista =  np.random.exponential(1/lambda_entrada,numero_de_aleatorios)
    tempo_proximo_lista = np.random.exponential(1/lambda_entrada,numero_de_aleatorios)
    print(entrada_lista)
    print(tempo_proximo_lista)

    fim = 0


    ##TODO: melhores nomes para as variáveis

    entrada = 0  ##tempo até a próxima entrada
    tempo_proximo = 0  ##tempo até terminar a execução no servidor


    while (1):

        if(i == numero_de_aleatorios and j == numero_de_aleatorios):
            esperanca = esperanca / tempo
            print('a número médio de pessoas no sistema é: ' + str(esperanca))
            return

        while(entrada == 0 and i < numero_de_aleatorios):
            entrada = int(entrada_lista[i])
            fila+= 1
            i += 1

        entrada -= 1

        ## while nescessário caso caia em um tempo = 0 novamente
        while(tempo_proximo == 0 and fila > 0 and j < numero_de_aleatorios):
            servidor = 1
            fila -= 1
            tempo_proximo = int(tempo_proximo_lista[j])
            j += 1
        if(fila == 0 and tempo_proximo == 0):
                servidor = 0
        else:
                tempo_proximo -= 1

        ##coisas inuteis para parar quando já tudo processado
        ##nunca será executável pois para depois da ultima remessa da entrada
        if(fim == 0):
            print('fila = ' + str(fila))
            print('servidor = ' + str(servidor))
        else:
            return
        if(not(fila > 0 or ( i < numero_de_aleatorios and j < numero_de_aleatorios))):
            fim = 1

        esperanca += fila + servidor ##soma o número de clientes no sistema
        tempo += 1  ##adiciona mais um no tempo

##executando a função main
main()
