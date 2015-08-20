# -*- coding: latin-1 -*-
__author__ = 'jorge'
import numpy as np
from operator import add


def pasta1():
    print('pasta1')

    #parametros
    lambda_entrada = 0.5    ##lambda do problema
    #numero_de_aleatorios = 10000 ##representa o número de variáveis aleatórias que irá ser gerado
    tempo_simulacao = 10000
    numero_ciclos= 10000
    exponencial_entrada = 0

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

        tempo_entre_entrada_vazio =  0
        tempo_vazio = 0

        total_vazio = 0

        total_saido = 0
        stasis = 0

        exponencial_entrada = 0

        while (1):

            #if(i == numero_de_aleatorios and j == numero_de_aleatorios):
                #esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                #media= media + esperanca/numero_ciclos
                ##tempo_entre_saida[:] = [x / total_saido for x in tempo_entre_saida]
                ##print('o tempo entre saida é:')
                ##print(tempo_entre_saida)
                ##tempo_entre_saida_final = map(add,tempo_entre_saida_final,tempo_entre_saida)
                ##tempo_entre_saida_final = tempo_entre_saida_final + np.array(tempo_entre_saida)
                ##tempo_entre_saida_final = [(x)/numero_ciclos for x in tempo_entre_saida]
            #    break
            if(tempo == tempo_simulacao):
                esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break



            while(entrada == 0):

                if(servidor == 0 ):
                    tempo_entre_entrada_vazio +=  exponencial_entrada
                    total_vazio += 1

                exponencial_entrada = np.random.exponential(1/lambda_entrada)

                entrada = int(exponencial_entrada) ##Gera uma nova entrada exponencial
                fila+= 1
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            while(tempo_proximo == 0 and fila > 0):
                servidor = 1
                fila -= 1
                ##aqui vamos colocar na lista o tempo que vai demorar
                total_saido += 1

                exponencial = np.random.exponential(1)
                tempo_proximo = int(exponencial) ##Gera um novo tempo exponencial
                ##tempo_entre_saida.append(stasis + exponencial)
                stasis = 0

                j += 1
            if(fila == 0 and tempo_proximo == 0):
                    ##aqui vamos contar o tempo da pessoa que saiu
                    tempo_vazio += 1
                    stasis +=1
                    servidor = 0
            else:
                    tempo_proximo -= 1

            ##coisas inuteis para parar quando já tudo processado
            ##nunca será executável pois para depois da ultima remessa da entrada


            esperanca += fila + servidor ##soma o número de clientes no sistema
            tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    #divisao_ciclos = np.array([numero_ciclos] * 100)

    #print(tempo_entre_saida)
    ##total = len(tempo_entre_saida)
    ##print(total)
    #y_temp = np.array(range(total))
    ##y = np.array(range(total))/total

    ##tempo_entre_saida.sort()

    tempo_vazio = tempo_vazio / tempo_simulacao
    tempo_entre_entrada_vazio = tempo_entre_entrada_vazio / tempo_simulacao
    total_vazio /= total_saido

    print(tempo_vazio)
    print(total_vazio)
    print(tempo_entre_entrada_vazio)

    return tempo_vazio,tempo_entre_entrada_vazio,total_vazio

def pasta2_correto():

    #parametros
    u_servidor = 1    ##U do servidor (tem que variar 1,1,5,2...10
    numero_ciclos= 1
    tempo_simulacao = 1000

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

        tempo_entre_entrada_vazio =  0
        tempo_vazio = 0

        total_vazio = 0

        total_entrada = 0
        total_saido = 0

        ultima_entrada = 0

        exponencial_entrada = 0
        exponencial_saida = 0

        total_entrada_vazio= 0

        aleatorio = np.random.random_sample()
        if(aleatorio > 0.1):
             volta = 1
        else:
             volta = 0

        while (1):



            if(tempo >= tempo_simulacao):
                esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break

            if(entrada == 0):

                if(servidor == 0 ):
                    total_entrada_vazio += 1
                total_entrada += 1

                exponencial_entrada = np.random.exponential(1/lambda_entrada)
                entrada = exponencial_entrada ##Gera uma nova entrada exponencial
                fila+= 1
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0


            if(tempo_proximo == 0 and fila > 0):
                servidor = 1

                fila -= 1

                if(volta == 1):
                    if(servidor == 0):
                        #tempo_entre_entrada_vazio +=  exponencial_entrada
                        total_entrada_vazio += 1
                    total_entrada += 1
                    fila += 1
                    ultima_entrada = tempo
                else:
                    total_saido +=1


                aleatorio = np.random.random_sample()
                if(aleatorio > 0.1):
                    volta = 1
                else:
                    volta = 0

                exponencial_saida = np.random.exponential(1/u_servidor)
                tempo_proximo = exponencial_saida
                j += 1
            if(fila == 0 and tempo_proximo == 0):
                servidor = 0
                if(volta == 1):
                    if(servidor == 0):
                        ##tempo_entre_entrada_vazio +=  exponencial_entrada
                        total_entrada_vazio += 1
                        servidor = 1
                    total_entrada += 1
                    fila += 1
                else:
                    total_saido +=1


                aleatorio = np.random.random_sample()
                if(aleatorio > 0.1):
                    volta = 1
                else:
                    volta = 0

                exponencial_saida = np.random.exponential(1/u_servidor)
                tempo_proximo = exponencial_saida
                j += 1
            else:
                    tempo_proximo -= 1
            ##coisas inuteis para parar quando já tudo processado
            ##nunca será executável pois para depois da ultima remessa da entrada
            esperanca += fila + servidor ##soma o número de clientes no sistema
            a = np.array([entrada,tempo_proximo])
            tempo_passado = np.min(a[np.nonzero(a)])

            if(servidor == 0):
                print(fila)
                tempo_vazio += tempo_passado


            #print('tempo entrada:' + str(entrada) + ' | tempo_proximo_esteira:' + str(tempo_proximo_esteira) + ' | tempo proximo_bicicleta' + str(tempo_proximo_bicicleta) + ' | tempo_passado:' + str(tempo_passado))

            entrada -= tempo_passado
            if(entrada != 0):
                entrada -= tempo_passado
            if(tempo_proximo != 0):
                tempo_proximo -= tempo_passado
            tempo += tempo_passado
            print(tempo)
            #tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    ##print("Media das medias: ", media)

    fracao_vazio = tempo_vazio / tempo
    fracao_entrada = total_entrada_vazio / total_entrada
    #tempo_entre_entrada_vazio = tempo_entre_entrada_vazio / tempo_simulacao
    total_vazio /= total_saido

    print('fração do tempo vazio ' + str(fracao_vazio))
    print('fração de entradas vazio ' + str(fracao_entrada))
    print(total_vazio)

    return fracao_vazio,fracao_entrada,total_vazio


def pasta2():
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

        tempo_entre_entrada_vazio =  0
        tempo_vazio = 0

        total_vazio = 0

        total_entrada = 0
        total_saido = 0

        ultima_entrada = 0

        exponencial_entrada = 0
        exponencial_saida = 0

        aleatorio = np.random.random_sample()
        if(aleatorio > 0.1):
             volta = 1
        else:
             volta = 0

        while (1):

            if(tempo == tempo_simulacao):
                esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break

            while(entrada == 0):

                if(servidor == 0 ):
                    tempo_entre_entrada_vazio +=  exponencial_entrada
                    total_vazio += tempo - ultima_entrada

                exponencial_entrada = np.random.exponential(1/lambda_entrada)
                entrada = int(exponencial_entrada) ##Gera uma nova entrada exponencial
                fila+= 1
                ultima_entrada = tempo
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0


            while(tempo_proximo == 0 and fila > 0):
                servidor = 1

                fila -= 1

                if(volta == 1):
                    if(servidor == 0):
                        tempo_entre_entrada_vazio +=  exponencial_entrada
                        total_vazio += tempo - ultima_entrada
                        total_entrada += 1
                    fila += 1
                    ultima_entrada = tempo
                else:
                    total_saido +=1


                aleatorio = np.random.random_sample()
                if(aleatorio > 0.1):
                    volta = 1
                else:
                    volta = 0

                exponencial_saida = np.random.exponential(1/u_servidor)
                tempo_proximo = int(exponencial_saida)
                resto += exponencial_saida - tempo_proximo
                if(resto > 1):
                    tempo_proximo += 1
                j += 1
            if(fila == 0 and tempo_proximo == 0):
                    tempo_vazio += 1
                    servidor = 0
            else:
                    tempo_proximo -= 1
            ##coisas inuteis para parar quando já tudo processado
            ##nunca será executável pois para depois da ultima remessa da entrada
            esperanca += fila + servidor ##soma o número de clientes no sistema
            tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    ##print("Media das medias: ", media)

    tempo_vazio = tempo_vazio / tempo_simulacao
    tempo_entre_entrada_vazio = tempo_entre_entrada_vazio / tempo_simulacao
    total_vazio /= total_saido

    print(tempo_vazio)
    print(tempo_entre_entrada_vazio)
    print(total_vazio)

    return tempo_vazio,tempo_entre_entrada_vazio,total_vazio

def pasta_3():
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

        tempo_entre_entrada_vazio =  0
        tempo_vazio = 0

        total_vazio = 0

        total_saido = 0

        ultima_entrada = 0

        exponencial_entrada = 0
        exponencial_saida = 0

        aleatorio = np.random.random_sample()
        if(aleatorio > 0.1):
             volta = 1
        else:
             volta = 0

        while (1):

            if(tempo == tempo_simulacao):
                esperanca = esperanca / tempo
                #print('a número médio de pessoas no sistema é: ' + str(esperanca))
                media= media + esperanca/numero_ciclos
                break

            while(entrada == 0):

                if(servidor == 0 ):
                    tempo_entre_entrada_vazio +=  exponencial_entrada
                    total_vazio += tempo - ultima_entrada

                exponencial_entrada = np.random.exponential(1/lambda_entrada)
                entrada = int(exponencial_entrada) ##Gera uma nova entrada exponencial
                fila+= 1
                ultima_entrada = tempo
                i += 1

            entrada -= 1

            ## while nescessário caso caia em um tempo = 0 novamente
            resto = 0


            while(tempo_proximo == 0 and fila > 0):
                servidor = 1

                fila -= 1

                if(volta == 1):
                    if(servidor == 0):
                        tempo_entre_entrada_vazio +=  exponencial_entrada
                        total_vazio += tempo - ultima_entrada
                    fila += 1
                    ultima_entrada = tempo

                aleatorio = np.random.random_sample()
                if(aleatorio > 0.1):
                    volta = 1
                else:
                    volta = 0

                exponencial_saida = np.random.exponential(1/u_servidor)
                tempo_proximo = int(exponencial_saida)
                resto += exponencial_saida - tempo_proximo
                if(resto > 1):
                    tempo_proximo += 1
                j += 1

            if(fila == 0 and tempo_proximo == 0 and servidor == 1):
                servidor = 0

                if(volta == 1):
                    if(servidor == 0):
                        tempo_entre_entrada_vazio +=  exponencial_entrada
                        total_vazio += tempo - ultima_entrada
                    fila += 1
                    ultima_entrada = tempo
                else:
                    total_saido +=1


                aleatorio = np.random.random_sample()
                if(aleatorio > 0.1):
                    volta = 1
                else:
                    volta = 0

                exponencial_saida = np.random.exponential(1/u_servidor)
                tempo_proximo = int(exponencial_saida)
                resto += exponencial_saida - tempo_proximo
                if(resto > 1):
                    tempo_proximo += 1
                j += 1

            if(fila == 0 and tempo_proximo == 0):
                    tempo_vazio += 1
                    servidor = 0
            else:
                    tempo_proximo -= 1
            ##coisas inuteis para parar quando já tudo processado
            ##nunca será executável pois para depois da ultima remessa da entrada
            esperanca += fila + servidor ##soma o número de clientes no sistema
            tempo += 1  ##adiciona mais um no tempo

    ##executando a função main
    ##print("Media das medias: ", media)

    tempo_vazio = tempo_vazio / tempo_simulacao
    tempo_entre_entrada_vazio = tempo_entre_entrada_vazio / tempo_simulacao
    total_vazio /= total_saido

    print(tempo_vazio)
    print(tempo_entre_entrada_vazio)
    print(total_vazio)

    return tempo_vazio,tempo_entre_entrada_vazio,total_vazio