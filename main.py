 # -*- coding: latin-1 -*-

__author__ = 'jorge'
import numpy as np
def main():
    lambda_entrada = 0.1
    fila = 0
    i = 0
    j = 0
    servidor = 0
    tempo_proximo = 0
    ##entrada_lista =  np.random.poisson(lambda_entrada,100)
    entrada_lista =  np.random.exponential(1/lambda_entrada,100)
    tempo_proximo_lista = np.random.exponential(1/lambda_entrada,100)
    print(entrada_lista)
    print(tempo_proximo_lista)
    fim = 0

    entrada = 0
    tempo_proximo = 0

    while (1):

        ##entrada = entrada_lista[i]
        while(entrada == 0 and i < 100):
            #fila += entrada
            ##print('passei aqui')
            entrada = int(entrada_lista[i])
            ##print('a entrada ficou' + str(entrada))
            fila+= 1
            i += 1

        entrada -= 1

        while(tempo_proximo == 0 and fila > 0 and j < 100):
            servidor = 1
            fila -= 1
            tempo_proximo = int(tempo_proximo_lista[j])
            j += 1
            ##print('j vale ' + str(j))
            ##print('tempo_proximo = ' + str(tempo_proximo))
        if(fila == 0 and tempo_proximo == 0):
                servidor = 0
        else:
                tempo_proximo -= 1

        ##if (servidor == 0):
        ##   if (fila > 0 and j < 100):
        ##        servidor = 1
        ##        fila -= 1
                ## checar ser random exponential é a função ideal para o caso
        ##        tempo_proximo = int(tempo_proximo_lista[j])
        ##        j += 1
        ##        print('tempo_proximo = ' + str(tempo_proximo))

        ##else:

        ##    tempo_proximo -= 1


        if(fim == 0):
            print('fila = ' + str(fila))
            print('servidor = ' + str(servidor))
        else:
            return
        if(not(fila > 0 or ( i < 100 and j < 100))):
            fim = 1

##executando a função main
main()
