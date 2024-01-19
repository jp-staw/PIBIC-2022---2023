from aux_functions import main_archives, soma
from functools import reduce
import os

# criando a tabela de informações

arquivos = main_archives()

for arquivo in arquivos:
    with open(arquivo, 'r') as arq:
        info = arq.readlines()[:7]
        info = [elemento.removesuffix('\n') for elemento in info]
        info = [elemento.split(':;')[1] for elemento in info]
        info.insert(0, '')
        info_completa = reduce(soma, info)

    with open('informações.txt', 'a') as arq:
        arq.write(info_completa)
        arq.write('\n')
