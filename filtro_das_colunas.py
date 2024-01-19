from aux_functions import main_archives, select_columns, mesh, lime
import pandas as pd
import matplotlib.pyplot as plt

arquivos = main_archives()

for arquivo in arquivos:
    with open(arquivos, '+a') as arq:
        conteudo = arq.readlines()
        conteudo = [i.split(';') for i in conteudo]
        conteudo = [select_columns(i, [0, 1, 3, 6, 7, 15, 18]) for i in conteudo]
        conteudo = [lime(i) for i in conteudo]
        conteudo = list(filter(lambda x: not x ==[], conteudo))
        conteudo = [mesh(i) for i in conteudo]
        arq.writelines(conteudo)

#'DDATA (YYYY-MM-DD)' 
#'HORA (UTC)'
#'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)'
#'RADIACAO GLOBAL (KJ/m²)'
#'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'
#'UMIDADE RELATIVA DO AR, HORARIA (%)'
#'VENTO, DIREÇÃO HORARIA (gr) (° (gr))'