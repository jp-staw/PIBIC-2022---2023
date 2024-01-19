from aux_functions import main_archives
import os

arquivos_das_estações_total = main_archives()

codigos_das_estações = [arquivo.split('_')[3] for arquivo in arquivos_das_estações_total]
diretorios = ['C:\\Users\\joaop\\Desktop\\Dados INMET\\Anos\\'+f'{2022-i}' for i in range(0,23)]

cabeçalho_das_estações = dict()


ja_foi = []
for diretorio in diretorios:
    os.chdir(diretorio)
    arquivos_no_ano = os.listdir()
    for codigo in codigos_das_estações:
        for arquivo in arquivos_no_ano:
            if codigo == arquivo.split('_')[3] and codigo not in ja_foi:
                ja_foi.append(codigo)
                with open(arquivo, 'r') as arq:
                    cabeçalho_das_estações[codigo] = arq.readlines()[0:7]

os.chdir('C:\\Users\\joaop\\Desktop\\Dados INMET\\Estacoes')

for arquivo in arquivos_das_estações_total:
    with open(arquivo, 'r+') as arq:
        conteudo = arq.readlines()
        arq.seek(0,0)
        arq.writelines(cabeçalho_das_estações.pop(arquivo.split('_')[3]) + ['DDATA (YYYY-MM-DD);HORA (UTC);PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB);RADIACAO GLOBAL (KJ/m²);TEMPERATURA DO AR - BULBO SECO, HORARIA (°C);UMIDADE RELATIVA DO AR, HORARIA (%);VENTO, DIREÇÃO HORARIA (gr) (° (gr));'] + conteudo)
