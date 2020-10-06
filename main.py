'''

    Threads: Produtor consumidor

    Autores : Mateus Soares
            : Rodrigo Pacheco
    Data    : 06 de outubro de 2020


'''

import threading
import random
import time

estoque = list()

trava = threading.Condition()

# Quantidade de produtos
prod_qtd = 3

# Tempo maximo para producao
tempo_max_prod = 3

# Tempo maximo para consumo
tempo_max_cons = 3

# Tamanho máximo estoque
estoque_max = 10

# Quantidade de produtores
prod_max = 3

# Quantidade de consumidores
cons_max = 3

def estoque_cheio():

    if len(estoque) == estoque_max:
        return True
    else:
        return False


def estoque_vazio():

    if len(estoque) == 0:
        return True
    else:
        return False


def produtor(ident):

    while True:
        for prod in range(1, prod_qtd+1):
            tempo = random.randint(1, tempo_max_prod)
            time.sleep(tempo)
            with trava:
                while estoque_cheio():
                    trava.notify()
                    trava.wait()
                estoque.append((ident, prod))
                print(f'Produtor {ident} armazena produto {prod}')


def consumidor(ident):

    while True:
        tempo = random.randint(1, tempo_max_cons)
        time.sleep(tempo)
        with trava:
            while estoque_vazio():
                trava.notify()
                trava.wait()
            prod = estoque.pop(0)
            print(f'Consumidor {ident} recebe produto {prod}')

if __name__ == '__main__':

    for i in range(1, prod_max+1):
        threading.Thread(target=produtor, args=(i,)).start()
    for i in range(1, prod_max+1):
        threading.Thread(target=consumidor, args=(i,)).start()