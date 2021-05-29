import random
import time
''' Metodo alternativo elegante 
a =[numeros, numeros, numeros]
b = a[:]
'''
sep = ('-' * 100)
print(f'\033[31m \033[0;0m')

def bubble_sort(lista):
    print(f'\033[30;1;47mLista desordenada\033[0;0m:\n', lista)
    lista_bubble = lista.copy()
    elementos = len(lista_bubble) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista_bubble[i] > lista_bubble[i + 1]:
                lista_bubble[i], lista_bubble[i + 1] = lista_bubble[i + 1], lista_bubble[i]
                ordenado = False
    print(sep)
    print('\033[1;32mBubble Sort\033[0;0m - lista ordenada:\n', lista_bubble)


def insertion_sort(lista):
    lista_insertion = lista.copy()
    for i in range(1, len(lista_insertion)):
        valor_atual = lista_insertion[i]
        posicao_atual = i
        while posicao_atual > 0 and lista_insertion[posicao_atual - 1] > valor_atual:
            lista_insertion[posicao_atual] = lista_insertion[posicao_atual - 1]
            posicao_atual = posicao_atual - 1

        lista_insertion[posicao_atual] = valor_atual
    print(sep)
    print(f'\033[1;33mInsertion Sort\033[0;0m - lista ordenada:\n', lista_insertion)


def shell_sort(lista):
    lista_shell = lista.copy()
    tamanho = len(lista_shell)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    intervalo = tamanho // 2
    while intervalo > 0:
        for i in range(intervalo, tamanho):
            valor_atual = lista_shell[i]
            posicao_atual = i
            while posicao_atual >= intervalo and lista_shell[posicao_atual - intervalo] > valor_atual:
                lista_shell[posicao_atual] = lista_shell[posicao_atual - intervalo]
                posicao_atual -= intervalo

            lista_shell[posicao_atual] = valor_atual
        intervalo //= 2
    print(sep)
    print(f'\033[1;36mShell Sort\033[0;0m - lista ordenada:\n', lista_shell)


def quick_sort(lista):
    pass
    lista_quick = lista.copy()

    print(sep)
    print(f'\033[1;34mQuick Sort\033[0;0m - lista ordenada:\n', lista_quick)


def merge_sort(lista):
    pass
    lista_merge = lista.copy()

    print(sep)
    print(f'\033[1;35mMerge Sort\033[0;0m - lista ordenada:\n', lista_merge)


def organizar_lista_randomica():
    # criacao da lista
    lista = []
    for i in range(100):
        lista.append(random.randint(1, 5000))

    # Execução dos algoritmos de ordenacao

    # Bubble Sort
    abertura_bubble = time.time()
    bubble_sort(lista)
    termino_bubble = time.time()
    total_blubble = (termino_bubble - abertura_bubble)
    print(f'Tempo \033[1;32mBubble Sort\033[0;0m:    \033[31m{total_blubble}\033[0;0m segundos')
    print(sep)

    # Insertion Sort
    abertura_insertion = time.time()
    insertion_sort(lista)
    termino_insertion = time.time()
    total_insert = (termino_insertion - abertura_insertion)
    print(f'Tempo \033[1;33mInsertion Sort\033[0;0m: \033[31m{total_insert}\033[0;0m segundos')
    print(sep)

    # Shell Sort
    abertura_shell = time.time()
    shell_sort(lista)
    termino_shell = time.time()
    total_shell = (termino_shell - abertura_shell)
    print(f'Tempo \033[1;36mShell Sort\033[0;0m:     \033[31m{total_shell}\033[0;0m segundos')
    print(sep)

    # Quick Sort
    abertura_quick = time.time()
    quick_sort(lista)
    termino_quick = time.time()
    total_quick = (termino_quick - abertura_quick)
    print(f'Tempo \033[1;34mQuick Sort\033[0;0m:     \033[31m{total_quick}\033[0;0m segundos')
    print(sep)

    # Merge Sort
    abertura_merge = time.time()
    merge_sort(lista)
    termino_merge = time.time()
    total_merge = (termino_merge - abertura_merge)
    print(f'Tempo \033[1;35mMerge Sort\033[0;0m:     \033[31m{total_merge}\033[0;0m segundos')
    print(sep)


organizar_lista_randomica()