 # -*- coding: latin-1 -*-

__author__ = 'jorge'
import numpy as np
def main():
    lambda_entrada = 5
    fila = 0
    servidor = 0
    tempo_proximo = 0

    while (1):
        entrada = np.random.poisson(lambda_entrada)
        fila += entrada
        if (servidor == 0):
            if (fila > 0):
                servidor = 1
                fila -= 1
                ## checar ser random exponential é a função ideal para o caso
                tempo_proximo = np.random.exponential(1 / lambda_entrada)
        else:
            tempo_proximo -= 1
        print('fila = ' + str(fila))
        print('servidor = ' + str(servidor))


##executando a função main
main()
