import json
from functions import clean_console

def binary_search(sequence, item):
    """PRIMEIRO ITEM DA LISTA"""
    first_value = int(sequence[0])
    """ÚLTIMO ITEM DA LISTA"""
    last_value = int(sequence[-1])
    found = False

    if item < first_value :
        print("Target is too small!")
        return None
    if item > last_value:
        print("Target is over the end index!")
        return None

    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        """Aqui ele "corta" e cria o midpoint"""
        midpoint = (begin_index + end_index) // 2
        """Aqui ele pega no midpoint criado e mete na variavel midpoint_value"""
        midpoint_string = sequence[midpoint]
        """Conversão de midpoint_string de string para int porque nao da para comparar strings com ints """
        midpoint_value = int(midpoint_string)

        print(f"Midpoint_value  is...", midpoint_value)

        if midpoint_value == item:
            print("Target found!")
            input("Press enter to exit...")
            clean_console()
            return midpoint
        
        elif item < midpoint_value:
            print("The target is before midpoint...")
            end_index = midpoint - 1
            print("Changing end_index...", end_index)
        elif item > midpoint_value:
            print("The target is after midpoint...")
            # aqui o begin_index deixa de ser o inicio da lista e passa a ser o inicio do midpoint+1
            begin_index = midpoint + 1
            print(f"Changing begin index to", begin_index)
    if not found:
         print(f"The {item} was not found!")
         
    return None

def linear_search(list, find):
    i = 0
    j = 0
    """ Aqui da uma volta no primeiro dict e outra volta no segundo dict"""
    for dict in list:
        for dict_values in dict.values():
            if dict_values == find:
                i = i + 1
                j = 1
                print(find + f" was found on the {i}º dictionary") 
                break
            else:
                continue
    
    if j == 0:
        print("Nothing was found...")


# ALPHABETIC_ORDER USING BUBBLE SORT #
def alphabetic_order():
        sort_keys = []
        try:        
            with open('data.json', 'r+') as file:
                data_base = json.load(file)
                tipo = input("Which one do you want to sort using bubble sort? Title, Director or Writer? ")

                if tipo in ["Title", "Director", "Writer"]:
                        for t in data_base:
                            sort_keys.append(t[tipo])
        

                        for i in range(len(sort_keys)):
                            for j in range(0, len(sort_keys) - i - 1):
                                if sort_keys[j] > sort_keys[j + 1]:
                                    sort_keys[j], sort_keys[j + 1] = sort_keys[j + 1], sort_keys[j]


                        print("List of items organized alphabetically: \n")
                        for n in sort_keys:
                                print(n)
                else:
                    print("Invalid Input!")
        except:
            print("File 'ni' found!")
            

