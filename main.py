import random
import time
from algoritmos_ordenacao import *

# Controladores para criação da lista
lista = []
quantidade_de_chaves = 7500
limite_max_algarismo = 5000


def ordenar_lista_randomica():
    # criacao da lista
    for i in range(quantidade_de_chaves):
        lista.append(random.randint(1, limite_max_algarismo))

    # Execução e calculo de tempo dos algoritmos de ordenação
    # Bubble Sort
    abertura_bubble = time.time()
    bubble_sort(lista)
    termino_bubble = time.time()
    total_blubble = (termino_bubble - abertura_bubble)
    print(f'Tempo \033[1;32mBubble Sort\033[0;0m:    \033[31m{total_blubble}\033[0;0m segundos')
    separador()

    # Insertion Sort
    abertura_insertion = time.time()
    insertion_sort(lista)
    termino_insertion = time.time()
    total_insert = (termino_insertion - abertura_insertion)
    print(f'Tempo \033[1;33mInsertion Sort\033[0;0m: \033[31m{total_insert}\033[0;0m segundos')
    separador()

    # Shell Sort
    abertura_shell = time.time()
    shell_sort(lista)
    termino_shell = time.time()
    total_shell = (termino_shell - abertura_shell)
    print(f'Tempo \033[1;36mShell Sort\033[0;0m:     \033[31m{total_shell}\033[0;0m segundos')
    separador()

    # Merge Sort
    abertura_merge = time.time()
    merge_sort(lista)
    termino_merge = time.time()
    total_merge = (termino_merge - abertura_merge)
    print(f'Tempo \033[1;35mMerge Sort\033[0;0m:     \033[31m{total_merge}\033[0;0m segundos')
    separador()

    # Quick Sort
    abertura_quick = time.time()
    quick_sort(lista)
    termino_quick = time.time()
    total_quick = (termino_quick - abertura_quick)
    print(f'Tempo \033[1;34mQuick Sort\033[0;0m:     \033[31m{total_quick}\033[0;0m segundos')
    separador()


ordenar_lista_randomica()
