from aux_functions import main_archives

arquivos = main_archives()

for arquivo in arquivos:
    with open(arquivo, 'r+') as arq:
        linhas = arq.readlines()
        arq.truncate(0)
        arq.seek(0,0)
        cabec, info = linhas[:8], linhas[8:]
        info = list(filter(lambda x: len(x.split(';')) == 8, info))
        info = [i.replace('/', '-').replace('00 UTC', ':00') for i in info]
        arq.writelines(cabec)
        arq.writelines(info)
    