import json
import os

def clean_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def title_id():
    print("List of every movie by id:")
    with open('data.json', 'r+') as file:
        data_base = json.load(file)

        for i in data_base:
            print(i["id"], i["Title"])
    file.close()

def newRegistry(new_movie):
    new_title = input("Title of the movie: ")
    new_movie["Title"] = new_title

    movie_release = input("Release date: ")
    new_movie["Release_date"] = movie_release

    movie_length = input("The length of the movie: ")
    new_movie["Movie_length"] = movie_length

    movie_diretor = input("Director of the movie: ")
    new_movie["Director"] = movie_diretor

    movie_writer = input("Writer of the movie: ")
    new_movie["Writer"] = movie_writer
    
def deleteJson(delete_movie):
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

def updateRegistry(update_movie, update_dict):
    
    update_movie["id"] = update_dict

    new_title = input("Title: ")
    update_movie["Title"] = new_title

    movie_release = input("The release date: ")
    update_movie["Release_date"] = movie_release

    movie_length = input("The length of the movie: ")
    update_movie["Movie_length"] = movie_length

    movie_diretor = input("Who wrote the movie: ")
    update_movie["Director"] = movie_diretor

    movie_writer = input("Writer of the movie: ")
    update_movie["Writer"] = movie_writer