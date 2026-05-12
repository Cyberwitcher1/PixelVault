import json
import string
import re

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


    def orgJson():
        # Carrega a informação
        with open('data.json', 'r+') as file:
            data_base = json.load(file)
            #Enumera cada dicionario
            data_base = [{**d,"id": i,} for i, d in enumerate(data_base)]

            print(data_base)
                
            # 3. vai para o fim da lista e da o dump
            file.seek(0)
            json.dump(data_base, file, indent=4)
            file.close()
            
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
        

        while True:
            password = "admin123"

            login_username = input("Insert the admin name: ")
            login_password = input("Insert the admin password: ")
            attempts = 3

            if re.search("[a-z]+", password) is None:
                print('At least one character must be in the range [a-z]')

            if re.search("[A-Z]+", password) is None:
                print('At least one character must be in the range [A-Z]')

            if re.search("[0-9]+", password) is None:
                print('At least one character must be in the range [0-9]')

            if re.search("[@#$]+", password) is None:
                print('At least one character must be in the range [a@#$]')

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
        def deleteJson():
            newList = []

            delete_movie = int(input("Escreva o id/filme que quer apagar: "))
            with open('data.json', 'r+') as file:
                mainList = json.load(file)
                del mainList[delete_movie]
                newList = mainList

                newList = [{"id": i, **d} for i, d in enumerate(newList)]
                file.seek(0)


            with open('data.json', 'w+') as file:
                json.dump(newList, file, indent=4)

        deleteJson()
        orgJson()


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
        print(5)

    if section == "6":
        print(6)



    if section == "7":
        print(2)



    if section == "8":
        menu == 0
        break


    



