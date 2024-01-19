import os

diretorios = {2000+i:f'C:\\Users\\joaop\\Desktop\\Dados INMET\\Anos\\{2000+i}' for i in range(0,23)}

for diretorio in diretorios:
    os.chdir(diretorios.get(diretorio))
    arquivos = os.listdir()
    for arquivo in arquivos:
        with open(arquivo, 'r') as arq:
            conteudo = arq.readlines()[9:]
            os.chdir('C:\\Users\\joaop\\Desktop\\Dados INMET\\Estacoes')
            with open(arquivo[:-28] + '.CSV', 'a') as arq_2:
                arq_2.writelines(conteudo)
        os.chdir(diretorios.get(diretorio))
