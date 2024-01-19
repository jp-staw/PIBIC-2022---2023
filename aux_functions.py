from math import isnan
from os import chdir, listdir
from functools import reduce
from pandas import DataFrame, read_csv

#Folder contendo funções que usualmente utilizo nos outros códigos, a maioria são referentes
# a quando estávamos ajustando os arquivos das estações

def main_archives():                                             # seleciona os arquivos principais dentro da pasta que estamos trabalhando
    chdir('C:\\Users\\joaop\\Desktop\\Dados INMET\\Estacoes')    # caso queira usar esses códigos, tem que mudar o caminho aonde está os arquivos
    return listdir()[2:]

def remove_blank_spaces(df:DataFrame) -> DataFrame:     # remove os espaços em branco das colunas
    df = filter(None, list(df))
    return DataFrame(list(df))

def std_filter(df:DataFrame, lower_bound, upper_bound): # Filtro do desvio padrão em alguma coluna
    f = lambda x: lower_bound <= float(x) <= upper_bound
    df = df[df.columns[0]].values.tolist()
    return DataFrame(filter(f, df))

def soma(a,b) -> str:                                   # apenas uma função para juntar duas strings
    return f'{a+b};'

def select_columns(lista, indices):                     # função que seleciona as colunas que estamos trabalhando
    return [lista[i] for i in indices]

def mesh(lista:list) -> str:                            # junta as informações das listas com informações adicionais
    lista.insert(0, '')
    return reduce(soma, lista)+'\n'

def lime(lista:list):                                   # função que remove a linha se ela estiver completamante em branco
    lista = [str(i).replace('-9999', '') for i in lista]
    copia = list(filter(lambda x: not (str(x) == ''), lista.copy()))
    if len(copia) < 3:
        lista.clear()
    else:
        pass
    return lista

#   area de teste
if __name__ == '__main__':
    pass
