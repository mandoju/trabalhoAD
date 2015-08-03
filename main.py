 # -*- coding: latin-1 -*-

__author__ = 'jorge'
import numpy as np
def main():
    lambda_entrada = 0.1
    fila = 0
    i = 0
    servidor = 0
    tempo_proximo = 0
    entrada_lista =  np.random.poisson(lambda_entrada,100)
    tempo_proximo_lista = np.random.exponential(1 / lambda_entrada,100)
    print(entrada_lista)
    print(tempo_proximo_lista)

    while (i < 100):
        entrada = entrada_lista[i]
        fila += entrada

        if(tempo_proximo == 0 and fila > 0):
            servidor = 0


        if (servidor == 0):
            if (fila > 0):
                servidor = 1
                fila -= 1
                ## checar ser random exponential é a função ideal para o caso
                tempo_proximo = int(tempo_proximo_lista[i])
                print('tempo_proximo = ' + str(tempo_proximo))

        else:

            tempo_proximo -= 1
        print('fila = ' + str(fila))
        print('servidor = ' + str(servidor))
        i += 1


##executando a função main
main()
