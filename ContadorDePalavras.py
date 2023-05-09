import unicodedata
import collections
import re

# Carrega o arquivo
with open('./arquivo.txt', 'r') as arquivo:
    texto = arquivo.read()

# Remove os acentos e exibe o texto reescrito
texto_sem_acentos = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
print('Texto reescrito sem acentos:')
print(texto_sem_acentos)

# Realiza a contagem das palavras
palavras = re.findall(r'\b\w+\b', texto_sem_acentos.lower())
contagem_palavras = collections.Counter(palavras)

# Ranqueia as palavras em forma decrescente
ranking_palavras = contagem_palavras.most_common()

# Exibe as palavras e suas respectivas contagens
print('Palavras ranqueadas em forma decrescente:')
for palavra, contagem in ranking_palavras:
    print(f'{palavra}: {contagem}')

# Permite ao usuário saber quais palavras deseja e quantas aparições de cada uma
while True:
    escolha = input('Digite a palavra que deseja saber a contagem ou 0 para sair: ')
    if escolha == '0':
        break
    elif escolha in contagem_palavras:
        print(f'A palavra "{escolha}" apareceu {contagem_palavras[escolha]} vezes no texto.')
    else:
        print(f'A palavra "{escolha}" não apareceu no texto.')

# Exibe a palavra com mais aparição e a com menos aparição
palavra_com_mais_aparicoes = ranking_palavras[0][0]
palavra_com_menos_aparicoes = ranking_palavras[-1][0]
print(f'A palavra com mais aparições é "{palavra_com_mais_aparicoes}" com {contagem_palavras[palavra_com_mais_aparicoes]} aparições.')
print(f'A palavra com menos aparições é "{palavra_com_menos_aparicoes}" com {contagem_palavras[palavra_com_menos_aparicoes]} aparições.')
