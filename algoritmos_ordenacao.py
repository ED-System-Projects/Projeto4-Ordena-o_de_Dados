def separador():
    quant = 200
    print('-' * quant)


# Bubble Sort
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
    separador()
    print('\033[1;32mBubble Sort\033[0;0m - lista ordenada:\n', lista_bubble)


# Insertion Sort
def insertion_sort(lista):
    lista_insertion = lista.copy()
    for i in range(1, len(lista_insertion)):
        valor_atual = lista_insertion[i]
        posicao_atual = i
        while posicao_atual > 0 and lista_insertion[posicao_atual - 1] > valor_atual:
            lista_insertion[posicao_atual] = lista_insertion[posicao_atual - 1]
            posicao_atual = posicao_atual - 1

        lista_insertion[posicao_atual] = valor_atual
    separador()
    print(f'\033[1;33mInsertion Sort\033[0;0m - lista ordenada:\n', lista_insertion)


# Shell Sort
def shell_sort(lista):
    lista_shell = lista.copy()
    tamanho = len(lista_shell)
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
    separador()
    print(f'\033[1;36mShell Sort\033[0;0m - lista ordenada:\n', lista_shell)


# Merge Sort
def merge_sort(lista):
    lista_merge = lista.copy()

    def merge(lista_sort):
        if len(lista_sort) > 1:
            metade = len(lista_sort) // 2
            esquerda = lista_sort[:metade]
            direita = lista_sort[metade:]
            merge(esquerda)
            merge(direita)
            i = j = k = 0
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    lista_sort[k] = esquerda[i]
                    i += 1
                else:
                    lista_sort[k] = direita[j]
                    j += 1
                k += 1
            while i < len(esquerda):
                lista_sort[k] = esquerda[i]
                i += 1
                k += 1
            while j < len(direita):
                lista_sort[k] = direita[j]
                j += 1
                k += 1

    merge(lista_merge)
    separador()
    print(f'\033[1;35mMerge Sort\033[0;0m - lista ordenada:\n', lista_merge)


# Quick Sort
def quick_sort(lista):
    lista_quick = lista.copy()

    def partition(lista_sort, menor, maior):
        i = (menor - 1)
        pivot = lista_sort[maior]  # pivô
        for j in range(menor, maior):
            if lista_sort[j] <= pivot:
                i = i + 1
                lista_sort[i], lista_sort[j] = lista_sort[j], lista_sort[i]
        lista_sort[i + 1], lista_sort[maior] = lista_sort[maior], lista_sort[i + 1]
        return i + 1

    def quick(lista_sort, menor, maior):
        if len(lista_sort) == 1:
            return lista_sort
        if menor < maior:
            pi = partition(lista_sort, menor, maior)
            quick(lista_sort, menor, pi - 1)
            quick(lista_sort, pi + 1, maior)

    quick(lista_quick, 0, len(lista_quick) - 1)
    separador()
    print(f'\033[1;34mQuick Sort\033[0;0m: - lista_sort ordenada:\n', lista_quick)



