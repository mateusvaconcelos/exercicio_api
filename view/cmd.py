from faixa import criar_faixa, salvar_faixa, ler_faixas

musica = input('Digite uma musica: ')
album = input('Digite o nome do album: ')
artista = input('Digite o nome do artista: ')

faixa1 = criar_faixa(musica, album, artista)

salvar_faixa(faixa1)

lista = ler_faixas()

for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["album"]} - {faixa["artista"]}')