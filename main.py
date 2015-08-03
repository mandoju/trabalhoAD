__author__ = 'jorge'
import numpy as np

def main():
    lambda_entrada = 5
    fila = 0
    servidor = 0


    while(1):
        entrada = np.random.poisson(lambda_entrada)
        fila += entrada
        if(servidor == 0):
            servidor = 1
            fila -= 1
        print(fila)

