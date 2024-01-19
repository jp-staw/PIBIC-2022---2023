from aux_functions import main_archives

# trocando vírgula por ponto nos arquivos

arquivos = main_archives()

for arquivo in arquivos:
    with open(arquivo, 'r+') as arq:
        conteudo = arq.readlines()
        conteudo[1:] = [i.replace(',','.') for i in conteudo[1:]]
        arq.seek(1,0)
        arq.writelines(conteudo)
