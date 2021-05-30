
# Bubble Sort
def bubble_sort(lista):
    elementos = len(lista) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
    separador()
    print('\033[1;32mBubble Sort\033[0;0m - lista ordenada:\n', lista)


# Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        posicao_atual = i
        while posicao_atual > 0 and lista[posicao_atual - 1] > valor_atual:
            lista[posicao_atual] = lista[posicao_atual - 1]
            posicao_atual = posicao_atual - 1

        lista[posicao_atual] = valor_atual
    separador()
    print(f'\033[1;33mInsertion Sort\033[0;0m - lista ordenada:\n', lista)


# Shell Sort
def shell_sort(lista):
    tamanho = len(lista)
    intervalo = tamanho // 2
    while intervalo > 0:
        for i in range(intervalo, tamanho):
            valor_atual = lista[i]
            posicao_atual = i
            while posicao_atual >= intervalo and lista[posicao_atual - intervalo] > valor_atual:
                lista[posicao_atual] = lista[posicao_atual - intervalo]
                posicao_atual -= intervalo

            lista[posicao_atual] = valor_atual
        intervalo //= 2
    separador()
    print(f'\033[1;36mShell Sort\033[0;0m - lista ordenada:\n', lista)


# Merge Sort
def merge_sort(lista):

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

    merge(lista)
    separador()
    print(f'\033[1;35mMerge Sort\033[0;0m - lista ordenada:\n', lista)


# Quick Sort
def quick_sort(lista):

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

    quick(lista, 0, len(lista) - 1)
    separador()
    print(f'\033[1;34mQuick Sort\033[0;0m: - lista ordenada:\n', lista)


def separador():
    quant = 200
    print('-' * quant)
