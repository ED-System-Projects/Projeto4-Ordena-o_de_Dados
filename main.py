import random
import time
from algoritmos_ordenacao import *

# Controladores para criação da lista
lista = []
quantidade_de_chaves = 15000
limite_max_algarismo = 5000


def criar_lista():
    if not lista:
        # criacao da lista
        for i in range(quantidade_de_chaves):
            lista.append(random.randint(1, limite_max_algarismo))
    else:
        print('A lista já foi criada, caso queira alterar delete a lista primeiro.')
    print(f'\033[30;1;47mLista Criada\033[0;0m:\n', lista)


def deletar_lista():
    if not lista:
        print(f'A lista já está vazia')
    else:
        lista.clear()
    print(f'\033[30;1;47mLista Deletada\033[0;0m:\n', lista)


# Execução e calculo de tempo dos algoritmos de ordenação
def ordenar_bubble(lista_bubble):
    lista_desordenada = lista_bubble.copy()
    # Bubble Sort
    abertura_bubble = time.time()
    bubble_sort(lista_desordenada)
    termino_bubble = time.time()
    total_blubble = (termino_bubble - abertura_bubble)
    print(f'Tempo \033[1;32mBubble Sort\033[0;0m:    \033[31m{total_blubble}\033[0;0m segundos.')
    separador()


def ordenar_insertion(lista_insertion):
    lista_desordenada = lista_insertion.copy()
    # Insertion Sort
    abertura_insertion = time.time()
    insertion_sort(lista_desordenada)
    termino_insertion = time.time()
    total_insert = (termino_insertion - abertura_insertion)
    print(f'Tempo \033[1;33mInsertion Sort\033[0;0m: \033[31m{total_insert}\033[0;0m segundos.')
    separador()


def ordenar_shell(lista_shell):
    lista_desordenada = lista_shell.copy()
    # Shell Sort
    abertura_shell = time.time()
    shell_sort(lista_desordenada)
    termino_shell = time.time()
    total_shell = (termino_shell - abertura_shell)
    print(f'Tempo \033[1;36mShell Sort\033[0;0m:     \033[31m{total_shell}\033[0;0m segundos.')
    separador()


def ordenar_merge(lista_merge):
    lista_desordenada = lista_merge.copy()
    # Merge Sort
    abertura_merge = time.time()
    merge_sort(lista_desordenada)
    termino_merge = time.time()
    total_merge = (termino_merge - abertura_merge)
    print(f'Tempo \033[1;35mMerge Sort\033[0;0m:     \033[31m{total_merge}\033[0;0m segundos.')
    separador()


def ordenar_quick(lista_quick):
    lista_desordenada = lista_quick.copy()
    # Quick Sort
    abertura_quick = time.time()
    quick_sort(lista_desordenada)
    termino_quick = time.time()
    total_quick = (termino_quick - abertura_quick)
    print(f'Tempo \033[1;34mQuick Sort\033[0;0m:     \033[31m{total_quick}\033[0;0m segundos.')
    separador()


while True:
    print(f'''
╔══════════════════════════╗
║           \033[1mMENU\033[0;0m           ║
║  (0) « \033[1mImprimir Lista\033[0;0m »  ║
║  (1) « \033[30;1;47mCriar Lista\033[0;0m »     ║
║  (2) « \033[30;1;41mDeletar Lista\033[0;0m »   ║
║  (3) « \033[1;32mBubble Sort\033[0;0m »     ║  
║  (4) « \033[1;33mInsertion Sort\033[0;0m »  ║      
║  (5) « \033[1;36mShell Sort\033[0;0m »      ║ 
║  (6) « \033[1;35mMerge Sort\033[0;0m »      ║ 
║  (7) « \033[1;34mQuick Sort\033[0;0m »      ║
║  (8)  « \033[30;1;46mComparar\033[0;0m »       ║
║  (9) « Configurações »   ║
║  (X)    « \033[1;31mSair\033[0;0m »         ║
╚══════════════════════════╝\n''')

    escolha = (input('Digita a opção escolhida: ').upper())
    if escolha == '0':
        print(lista)
        continue

    elif escolha == '1':
        print('Criando uma lista...')
        criar_lista()
        continue

    elif escolha == '2':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Deletando a lista...')
            deletar_lista()
        continue

    elif escolha == '3':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Bubble Sort...')
            ordenar_bubble(lista)
        continue

    elif escolha == '4':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Insertion Sort...')
            ordenar_insertion(lista)
        continue

    elif escolha == '5':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Shell Sort...')
            ordenar_shell(lista)
        continue

    elif escolha == '6':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Merge Sort...')
            ordenar_merge(lista)
        continue

    elif escolha == '7':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Quick Sort...')
            ordenar_quick(lista)
        continue

    elif escolha == '8':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Comparando Algoritmos...')
            ordenar_bubble(lista)
            ordenar_insertion(lista)
            ordenar_shell(lista)
            ordenar_merge(lista)
            ordenar_quick(lista)
        continue

    elif escolha == '9':
        quantidade_de_chaves = int(input('Quantidade de Chaves da Lista\n (Padrão: 15000): '))
        limite_max_algarismo = int(input('Limite Máximo de Algarismo\n (Padrão: 5000): '))
        print('Configurações Salvas...')
        continue

    elif escolha == 'X':
        print('Finalizando o programa...')
        break

    else:
        print('Somente comandos disposto no MENU funcionam, boa tentativa meu chapa...')
