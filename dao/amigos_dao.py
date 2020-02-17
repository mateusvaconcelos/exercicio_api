def criar_faixa(musica, album, artista):
    faixa = {'musica': musica, 'album':album, 'artista':artista }
    return faixa

def salvar_faixa(faixa):
    arquivo = open('Aula16/faixas.txt','a')
    arquivo.write(f'{faixa["musica"]};{faixa["album"]};{faixa["artista"]}\n')
    arquivo.close()

def ler_faixas():
    arquivo = open('Aula16/faixas.txt','r')
    lista_faixas = []
    for linha in arquivo:
        linha = linha.strip()
        dados_faixa = linha.split(';')
        faixa = criar_faixa(dados_faixa[0], dados_faixa[1], dados_faixa[2])
        lista_faixas.append(faixa)
    arquivo.close()
    return lista_faixas