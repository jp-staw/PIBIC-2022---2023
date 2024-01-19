import pandas as pd
import matplotlib.pyplot as plt
from aux_functions import main_archives, remove_blank_spaces, std_filter

arquivos = main_archives()

for arquivo in arquivos:
    arq = pd.read_csv(arquivo, encoding='latin-1', sep=';', na_values='', low_memory=False, skip_blank_lines=True)
    coluna = arq['PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)']
    mean = coluna.mean()
    std = coluna.std()
    N = 3
    lower_bound = mean-N*std
    upper_bound = mean+N*std

    fig, axs = plt.subplots(1, 2, sharey= True)
    fig.suptitle(f'{arquivo}')

    coluna = std_filter(coluna, lower_bound, upper_bound)

    axs[0].plot(coluna)

    axs[1].hist(coluna, bins=400, orientation='horizontal', range=(lower_bound, upper_bound), histtype = 'stepfilled')

    plt.savefig(f'C:\\Users\\joaop\\Desktop\\Dados INMET\\Estacoes\\histogramas\\{arquivo}.png')
    plt.clf()
    plt.close()
