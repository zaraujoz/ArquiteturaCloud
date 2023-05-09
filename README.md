# ArquiteturaCloud
Foi usado para mostrar as palavras e suas respectivas contagens, utilizei um loop 'for' para passar a lista de palavras ranqueadas e mostrar cada palavra e sua contagem.

Para dar permissão ao usuário saber quais palavras deseja e quantas aparições de cada uma, utilizamos um loop while que faz com que o usuário que digite a palavra desejada. Se o usuário digitar 0, o loop é interrompido. Do contrário, a contagem da palavra é exibida, se a palavra estiver presente no texto, ou uma mensagem de que a palavra não foi encontrada, caso contrário.

Por fim, para exibir a palavra com mais aparições e a com menos.

No código acima, utilizamos a função unicodedata.normalize() para deletar os acentos do texto, a função re.findall() para separar as palavras do texto e a classe collections.Counter() para contar as palavras. Além disso, utilizamos a função most_common() para ranquear as palavras em forma decrescente.