from aux_functions import main_archives, std_filter
import pandas as pd

# incluindo os momentos estatísticos na tabela de informações

arquivos = main_archives()

infos = dict()

for arquivo in arquivos:
    arq = pd.read_csv(arquivo, encoding='latin-1', sep=';',na_values='', header=7, na_filter=False, low_memory=False)
    coluna = arq[arq.columns[2]]
    coluna = pd.DataFrame(filter(lambda x: not (str(x) == ''), coluna)).astype(float)
    for _ in range(2):
        media = coluna.mean().tolist()[0]
        stdev = coluna.std().tolist()[0]
        N = 4
        lower_bound = media-N*stdev
        upper_bound = media+N*stdev

        coluna = std_filter(coluna, lower_bound, upper_bound)

    infos[f'{arquivo}'] = f'{coluna.mean().tolist()[0]};{coluna.std().tolist()[0]};{coluna.skew().tolist()[0]};{coluna.kurt().tolist()[0]};{coluna.count().tolist()[0]};'


with open('informações.txt', 'r+') as arq:
    linhas = arq.readlines()
    linhas = [i.removesuffix('\n') + infos.get(j) + '\n' for i, j in zip(linhas, infos)]
    arq.seek(0,0)
    arq.writelines(linhas)

#REGIAO;UF;ESTACAO;CODIGO (WMO);LATITUDE;LONGITUDE;ALTITUDE;<P>;std;skew;kurtosis;Numero de dados;
