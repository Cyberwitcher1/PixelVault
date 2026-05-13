import json
import os
from searches import binary_search, linear_search, alphabetic_order
from functions import title_id, newRegistry, deleteJson, orgJson, updateRegistry, clean_console

menu=1

while (menu==1):
    print("|========|Menu|========")
    print("1 - Add a movie")
    print("2 - Update a movie")
    print("3 - Remove a movie")
    print("4 - Show all movies")
    print("5 - Show all movies by alphabetic order")
    print("6 - Linear search")
    print("7 - Binary search (in ordered data)")
    print("8 - Exit")
    section = input("Please noble hero, choose one of the sections: ")
    data_base = []
    new_base = []
    new_movie = {}
    update_movie = {}

################################# - M E N U - ########################################
            
    if section == "1":
        clean_console()
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
        newRegistry(new_movie)
        writeJson()
        clean_console()
        print("New movie added!")
        input("Press enter to exit...")
        clean_console()
        
    """ ATUALIZAR """
    if section == "2":
            clean_console()
            title_id()

            with open('data.json', 'r+') as file:
                data_base = json.load(file)
                update_dict = int(input("What movie/id do you want to update?"))
                clean_console()
                file.close()
                            

            updateRegistry(update_movie, update_dict)

            with open('data.json', 'r+') as file:
                data_base = json.load(file)
                data_base[update_dict] = update_movie
                new_base = data_base
                file.close()
            with open ('data.json', 'w') as file:
                json.dump(new_base, file, indent=4)
                clean_console()
                print("Update sucessful!")
                input("Press enter to exit...")
                file.close()
                clean_console()

    """ REMOVER """
    if section == "3":
        clean_console()
        title_id()
        delete_movie = int(input("Which id do you want to remove?: "))

        while True:
            del_confirmation = input("Are you sure that you want to delete it? If yes, write: 'IAMSURE' if you wrote by mistake, write: 'NO': ")
            if del_confirmation == "IAMSURE":
                deleteJson(delete_movie)
                orgJson()
                clean_console()
                print("Delete completed!")
                input("Click enter to exit...")
                clean_console()
                break
            elif del_confirmation == "NAO":
                print("The dictionary wasnt deleted...")
                break
            else:
                print("Invalid Input!")



    """" MOSTRAR TUDO """
    if section == "4":
        clean_console()
        while True:
            esc = input("Do you want any filter?(YES/NO): ")
            clean_console()

            # SEM FILTRO
            if esc == "NO" or esc == "no":
                with open('data.json', 'r') as file:
                    data_base = json.load(file)
                print(data_base)
                break
            # COM FILTRO    
            elif esc == "YES" or esc == "yes":
                filter = input("What filter do you want to apply(Title, Release_date, Movie_Length, Director, Writer): ")
                clean_console()
                print("List of movies with the applied filter:")

                with open('data.json', 'r') as file:
                    data_base = json.load(file)
                for dict in data_base:
                    print(dict[filter])
                break
            else:
                print("Invalid input You have to write yes or no...!")

        input("\nClick enter to exit...")
        clean_console()
                
    if section == "5":
        clean_console()
        alphabetic_order()
        input("\nPress enter to exit...")
        clean_console()
                
    if section == "6":
            clean_console()       
            with open('data.json', 'r') as file:
                data_base = json.load(file)

                search_list = data_base
                find = input("Write what you are looking for: ")
                linear_search(search_list, find)
            file.close()
    
    if section == "7":
        clean_console()
        sequence_a = []

        with open('data.json', 'r') as file:
            data_base = json.load(file)

            filter = "id"

            for dict in data_base:
                sequence_a.append(dict[filter])
                
        item_a = int(input("Choose the id that you want: "))
        binary_search(sequence_a, item_a)

    if section == "8":
        clean_console()
        print("Until a next time valiant hero! With great bifanas, comes great responsibility - Uncle Ben")
        input()
        menu == 0
        break


    



