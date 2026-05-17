Como funciona:
O InfinityBox é um sistema de gestão de filmes da Marvel por linha de comandos onde permite gerir o teu catálogo de filmes localmente num ficheiro JSON.

Aspectos principais da aplicação:
- Gestão de e manipulação dados 
- Filtros, listagem, estátistica
- Utilização diversa de algoritmia

Como usar a Gestão de dados do InfinityBox:
1 - Add movie - deixa adicionar ou criar um registo novo
2 - Update movie - permite atualizar um filme a tua escolha
3 - Remove movie - permite remover um filme
4 - Show all movies - permite ver todos os filmes com um filtro a tua escolha
5 - Show all movies by alphabetic order(Bubble Sort) - da-te três opções para poderes fazer o bubble sort da tua lista de filmes da marvel
6 - Show all movies release dates with Quick Sort - Mostra todas as release dates organizadas com quick sort
7 - Linear search - Faz uma pesquisa linear
8 - Binary search (in ordered data) - faz uma pesquisa binária para ver se existe na lista o que queres procurar(id, Release_date ou Movie length)
9 - Statistics - Mostra a media e o total de filmes da base de dados/biblioteca de filmes
10 - Regex test search - Permite fazer um regex search com a um title que queiras ver se existe na tua biblioteca!
11 - Exit - Fechar o programa


Jornada:
Os primeiros passos do projecto foi estruturar com o while e criando o menu com maior parte das opções pretendidas do enunciado. De seguida foi conseguir dar o dump para o ficheiro json da maneira que eu queria, ou seja, uma lista de dicionários, porque achei a melhor formata para o projecto em si, e pra já uma estruturas mais simplificada chegava, mas existe a possibilidade de uma dia querer acrescentar series por exemplo, mas o meu foco neste projecto era mais os filmes e a fluidez de acrescentar, remover, ordenar, etc, filtros, resumidamente o foco seria mais a algoritimia.

Depois criei e desenvolvi o CRUD, onde demorei uma boa parte do projecto, maoritariamente por causa da organização e geração automática do id, mas felizmente consegui ir resolver alguns obstáculos que tive. Eventualmente também separei as funções do menu, criando o ficheiro searches.py para pesquisas e com alguma parte do sorting, e as maior parte das funções coloquei no functions.py. O atualizar dos dados também foi uma boa aprendizagem, não tanto pela lógica mas por ter que refazer a lista de dicionários e voltar a por dentro do json, e perceber em concreto o with open, dump, etc, ou seja a exportação para ficheiros json.

Um bom desafio para mim foi também fazer o linear e o binary search, dando mais relevância ao binary, especialmente de maneira a que corresse bem dentro do programa e da maneira que eu queria. Tive alguma dificuldade em finalizar o binary search porque algo na lógica não estava bem, inicialmente achei que pelas datas estavam a ser mal comparadas em vez de ser com números de index e a não fazer o desampocatamento bem, mas acabei por perceber que estava era sempre a colocar que não realmente não existia, conseguindo solucionar quando esse valor não fosse encontrado e que retornasse um print na consola.

Quick sort para mim também foi uma otima dileberada, escolhi-o como segundo para tentar fazer o algoritmo mais dificil que houvesse nos critérios do projeto, o que acabou por ser bastanta intuitivo e mais fácil daquilo que inicialmente esperava, o que mais o diferenciou foi o facto de ter que ser uma função recursiva, ou seja a lista ou a sequência ten que vir de fora da função e acabou por excelente escolha. Por fim, acabo por dizer que ainda há espaço para aprofundar, e polir mais algum tipo de bugs que possa existir, mas de resto adorei fazer o projeto e acredito que foi o mais produtivose o mais enriquecidor a nivel acadêmico que já tive até agora. 



