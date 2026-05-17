import json, os, re
from searches import binary_search, linear_search, alphabetic_order, regex_title
from functions import title_id, newRegistry, deleteJson, orgJson, updateRegistry, clean_console, writeJson, average_time

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
    print("8 - Statistics")
    print("9 - Regex testing")
    print("10 - Exit")
    section = input("Choose one of the sections: ")
    data_base = []
    new_base = []
    new_movie = {}
    update_movie = {}


################################# - M E N U - ########################################
    """ ADD """
    if section == "1":
        clean_console()
        # Registo novo
        newRegistry(new_movie)
        writeJson(new_movie)
        clean_console()
        print("New movie added!")
        input("Press enter to exit...")
        clean_console()
        
    """ UPDATE """
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


    """ REMOVE """
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

    """" SHOW ALL """
    if section == "4":
        clean_console()
        while True:
            esc = input("Do you want any filter?(YES/NO): ")
            clean_console()

            # WITH FILTER
            if esc == "NO" or esc == "no":
                with open('data.json', 'r') as file:
                    data_base = json.load(file)
                print(data_base)
                break
            # WITHOUT FILTER   
            elif esc == "YES" or esc == "yes":
                filter = input("What filter do you want to apply(Title, Release_date, Movie_Length, Director, Writer): ")
                clean_console()
                print("List with the applied filter:")

                with open('data.json', 'r') as file:
                    data_base = json.load(file)
                for dict in data_base:
                    print(dict[filter])
                break
            else:
                print("Invalid input You have to write yes or no...!")

        input("\nClick enter to exit...")
        clean_console()
    """" SHOW ALL - ALPHABETIC ORDER """            
    if section == "5":
        clean_console()
        alphabetic_order()
        input("\nPress enter to exit...")
        clean_console()
    """" LINEAR SEARCH """
    if section == "6":
            clean_console()       
            with open('data.json', 'r') as file:
                data_base = json.load(file)

                search_list = data_base
                find = input("Write what you are looking for: ")
                linear_search(search_list, find)
            file.close()
    """ BINARY SEARCH """
    if section == "7":
        clean_console()
        sequence = []
        with open('data.json', 'r') as file:
            data_base = json.load(file)
            filter_id = "id"
            filter_date = "Release_date"
            filter_length = "Movie_length"

        filter = input("Which of the data do you want to do a Binary search?(id, Release date, Movie length?)")

        if filter == "id":
            for dict in data_base:
                sequence.append(dict[filter_id])                     
            item_a = int(input("Choose the id do you want to find: "))
        elif filter == "Release date":
            for dict in data_base:
                sequence.append(dict[filter_date])
                sequence.sort()
            item_a = int(input("Which date you want to find?"))
            clean_console()

        elif filter == "Movie length":
            for dict in data_base:
                sequence.append(dict[filter_length])
                sequence.sort()
            item_a = int(input("Which movie length are you looking for?"))
            clean_console()
        else:
            print("Wrong input!")
        
        binary_search(sequence, item_a)
    """ STATISTICS"""
    if section == "8":
        average_time()
    """ REGEX """
    if section == "9":
        clean_console()
        regex_title()

    if section == "10":
        clean_console()
        print("Until a next time brave hero! With great bifanas, comes great responsibility - Uncle Ben")
        input()
        menu == 0
        break


    



