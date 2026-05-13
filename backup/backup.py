import json

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
    section = input("Escolha uma das opções: ")
    data_base = []
    new_base = []
    new_movie = {}

    def title_id():
        print("Lista de todos os filmes por id:")
        with open('data.json', 'r+') as file:
            mainList = json.load(file)

            for i in mainList:
                print(i["id"], i["Titulo"])
        file.close()

    def newRegistry():
        new_title = input("O título: ")
        new_movie["Titulo"] = new_title

        movie_release = input("O ano de lançamento: ")
        new_movie["Lancamento"] = movie_release

        movie_length = input("A longevidade: ")
        new_movie["Tempo"] = movie_length

        movie_diretor = input("O diretor do filme: ")
        new_movie["Diretor"] = movie_diretor

        movie_writer = input("O escritor do filme: ")
        new_movie["Escritor"] = movie_writer
        
    def deleteJson():
        newList = []
        with open('data.json', 'r+') as file:
            mainList = json.load(file)
            del mainList[delete_movie]
            newList = mainList

            newList = [{"id": i, **d} for i, d in enumerate(newList)]
            file.seek(0)
        file.close()

        with open('data.json', 'w+') as file:
            json.dump(newList, file, indent=4)
        file.close()


    def orgJson():
        # Carrega a informação
        with open('data.json', 'r+') as file:
            data_base = json.load(file)
            #Enumera cada dicionario
            data_base = [{**d,"id": i,} for i, d in enumerate(data_base)]
                
            # 3. vai para o fim da lista e da o dump
            file.seek(0)
            json.dump(data_base, file, indent=4)
            file.close()

################################# - M E N U - ########################################
            
    if section == "1":        
        def writeJson():
            # Carrega a informação
            with open('data.json', 'r+') as file:
                data_base = json.load(file)

                # 2. Adiciona o filme novo a lista
                data_base.append(new_movie)

                #Enumera cada dicionario
                data_base = [{"id": i, **d} for i, d in enumerate(data_base)]
                
                # 3. vai para o fim da lista e da o dump
                file.seek(0)
                json.dump(data_base, file, indent=4)
                file.close()
        # Registo novo
        newRegistry()
        writeJson()
        
    """ ATUALIZAR """
    if section == "2":
        
            title_id()

            with open('data.json', 'r+') as file:
                data_base = json.load(file)
                update_dict = int(input("Qual é o id/filme que quer atualizar?"))
                print(data_base[update_dict])
                file.close()
                            

                
            def updateRegistry():
                new_movie["id"] = update_dict

                new_title = input("O título: ")
                new_movie["Titulo"] = new_title

                movie_release = input("O ano de lançamento: ")
                new_movie["Lancamento"] = movie_release

                movie_length = input("A longevidade: ")
                new_movie["Tempo"] = movie_length

                movie_diretor = input("O diretor do filme: ")
                new_movie["Diretor"] = movie_diretor

                movie_writer = input("O escritor do filme: ")
                new_movie["Escritor"] = movie_writer


            updateRegistry()

            with open('data.json', 'r+') as file:
                data_base = json.load(file)
                data_base[update_dict] = new_movie
                new_base = data_base
                print(new_base)
                file.close()
            with open ('data.json', 'w') as file:
                print(new_base)
                json.dump(new_base, file, indent=4)
                file.close()

    """ REMOVER """
    if section == "3":
        title_id()
        delete_movie = int(input("Escreva o id/filme que quer apagar: "))

        while True:
            del_confirmation = input("Quer MESMO apagar? Se sim, escreva: 'EUQUEROAPAGAR' ou se enganou-se escreva 'NAO': ")
            if del_confirmation == "EUQUEROAPAGAR":
                deleteJson()
                orgJson()
                print("Delete concluido!")
                break
            elif del_confirmation == "NAO":
                print("O dicionário não foi deletado...")
                break
            else:
                print("Input inválido!")

    """" MOSTRAR TUDO """
    if section == "4":
        while True:
            esc = input("Quer algum filtro? (SIM/NAO)")
            # SEM FILTRO
            if esc == "NAO" or esc == "nao":
                with open('data.json', 'r') as file:
                    data_base = json.load(file)
                print(data_base)
                break
            # COM FILTRO    
            elif esc == "SIM" or esc == "sim":
                filter = input("Que filtro quer aplicar(Título,Lancamento,Tempo,Diretor,Escritor): ")

                with open('data.json', 'r') as file:
                    data_base = json.load(file)
                for dict in data_base:
                    print(dict[filter])
                break
            else:
                print("Tem que escrever Sim ou Não!")        
    if section == "5":
        target = input("Escreva o que quer procurar: ")





    if section == "6":
            def linear_search(list, find):
                i = 0
                """ Aqui da uma volta no primeiro dict e outra volta no segundo dict"""
                for dict in list:
                    for dict_values in dict.values():
                        if dict_values == find:
                            i = i + 1
                            print(find + f" was found on the {i}º dictionary")
                            
                            break
                        else:
                            continue
                        
            with open('data.json', 'r') as file:
                data_base = json.load(file)

                search_list = data_base
                find = input("Escreva o que quer procurar: ")
                linear_search(search_list, find)
            file.close()
    
    if section == "7":
        sequence_a = []

        with open('data.json', 'r') as file:
            data_base = json.load(file)

            filter = "id"

            for dict in data_base:
                sequence_a.append(dict[filter])
                print(sequence_a)

        def binary_search(sequence, item):
            begin_index = 0
            end_index = len(sequence) - 1

            while begin_index <= end_index:
                """Aqui ele "corta" e cria o midpoint"""
                midpoint = begin_index + (end_index - begin_index) // 2
                """Aqui ele pega no midpoint criado e mete na variavel midpoint_value"""
                midpoint_value = sequence[midpoint]
                print(f"Midpoint  is...", midpoint_value) 
                if midpoint_value == item:
                    print("Target found!")
                    return midpoint
                elif item < midpoint_value:
                    print("The target is before midpoint...")
                    end_index = midpoint - 1
                    print("Changing end_index...", end_index)
                else:
                    print("The target is after midpoint...")
                    """aqui o begin_index deixa de ser o inicio da lista e passa a ser o inicio do midpoint+1"""
                    begin_index = midpoint + 1
                    print(f"Changing begin index...", begin_index)
            return None
        
    item_a = int(input("Escreva o valor do id que pretende: "))
    binary_search(sequence_a, item_a)

    if section == "8":
        menu == 0
        break

