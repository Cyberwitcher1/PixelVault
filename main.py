import json
dados = []


filmes = {
}

menu=1

while (menu==1):
    print("|========|Menu|========")
    print("1 - Adicionar um filme")
    print("2 - Atualizar um filme")
    print("3 - Remover um filme")
    print("4 - Mostrar todos os filmes")
    print("5 - Mostrar todos os filmes por ordem alfabética")
    print("6 - Pesquisa linear")
    print("7 - Pesquisa binária (em dados ordenados)")
    print("8 - Sair")
    escolha = input("Escolha uma das opções: ")
    
    if escolha == "1":

        #ENTRETINEMENTO 
        def criarRegistos():
            registo_titulo = input("O título: ")
            filmes["Titulo"] = registo_titulo
            registo_lancamento = input("O ano de lançamento: ")
            filmes["Lancamento"] = registo_lancamento
            registo_tempo = input("A longevidade: ")
            filmes["Tempo"] = registo_tempo
            registo_diretor = input("O diretor do filme: ")
            filmes["Diretor"] = registo_diretor
            registo_escritor = input("O escritor do filme: ")
            filmes["Escritor"] = registo_escritor

        ## Achei que é melhor user f do que fp por ser mais rápido, em vez de escrever uma string para a memória ele aponto pro ficheiro e passa logo pra lá
        def escrever_json():
            with open('dados.json', 'w') as f:
                json.dump(filmes, f)

        criarRegistos()
        escrever_json()
        


    if escolha == "2":
        # dictionary.update(other)
        print("teste")
    if escolha == "3":
        print("teste3")
    if escolha == "4":
        print(filmes)

        for x in filmes: 
            print(x)
            print(filmes[x])

    if escolha == "5":
        print("teste5")
    if escolha == "6":
        print("teste6")
    if escolha == "7":
        print("teste7")
    if escolha == "8":
        menu == 0
        break


    



