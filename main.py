 # -*- coding: latin-1 -*-

__author__ = 'jorge'
import numpy as np
def main():


    #parametros
    lambda_entrada = 0.1    ##lambda do problema
    numero_de_aleatorios = 100 ##representa o n�mero de vari�veis aleat�rias que ir� ser gerado

    fila = 0
    i = 0
    j = 0
    servidor = 0
    tempo_proximo = 0

    ##vari�veis para calcular a m�dia
    tempo = 0
    esperanca = 0

    ##entrada_lista =  np.random.poisson(lambda_entrada,100)

    entrada_lista =  np.random.exponential(1/lambda_entrada,numero_de_aleatorios)
    tempo_proximo_lista = np.random.exponential(1/lambda_entrada,numero_de_aleatorios)
    print(entrada_lista)
    print(tempo_proximo_lista)

    fim = 0


    ##TODO: melhores nomes para as vari�veis

    entrada = 0  ##tempo at� a pr�xima entrada
    tempo_proximo = 0  ##tempo at� terminar a execu��o no servidor


    while (1):

        if(i == numero_de_aleatorios and j == numero_de_aleatorios):
            esperanca = esperanca / tempo
            print('a n�mero m�dio de pessoas no sistema �: ' + str(esperanca))
            return

        while(entrada == 0 and i < numero_de_aleatorios):
            entrada = int(entrada_lista[i])
            fila+= 1
            i += 1

        entrada -= 1

        ## while nescess�rio caso caia em um tempo = 0 novamente
        while(tempo_proximo == 0 and fila > 0 and j < numero_de_aleatorios):
            servidor = 1
            fila -= 1
            tempo_proximo = int(tempo_proximo_lista[j])
            j += 1
        if(fila == 0 and tempo_proximo == 0):
                servidor = 0
        else:
                tempo_proximo -= 1

        ##coisas inuteis para parar quando j� tudo processado
        ##nunca ser� execut�vel pois para depois da ultima remessa da entrada
        if(fim == 0):
            print('fila = ' + str(fila))
            print('servidor = ' + str(servidor))
        else:
            return
        if(not(fila > 0 or ( i < numero_de_aleatorios and j < numero_de_aleatorios))):
            fim = 1

        esperanca += fila + servidor ##soma o n�mero de clientes no sistema
        tempo += 1  ##adiciona mais um no tempo

##executando a fun��o main
main()
