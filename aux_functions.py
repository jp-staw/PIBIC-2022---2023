from math import isnan
from os import chdir, listdir
from functools import reduce
from pandas import DataFrame, read_csv

def main_archives():
    chdir('C:\\Users\\joaop\\Desktop\\Dados INMET\\Estacoes')
    return listdir()[2:]

def remove_blank_spaces(df:DataFrame) -> DataFrame:
    df = filter(None, list(df))
    return DataFrame(list(df))

def std_filter(df:DataFrame, lower_bound, upper_bound):
    f = lambda x: lower_bound <= float(x) <= upper_bound
    df = df[df.columns[0]].values.tolist()
    return DataFrame(filter(f, df))

def soma(a,b) -> str:
    return f'{a+b};'

def select_columns(lista, indices):
    return [lista[i] for i in indices]

def mesh(lista:list) -> str:
    lista.insert(0, '')
    return reduce(soma, lista)+'\n'

def lime(lista:list):
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