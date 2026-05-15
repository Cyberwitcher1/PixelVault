import json
from functions import clean_console

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    """VERIFICAR O ULTIMO DIGITO"""
    print(sequence)
    last_item = sequence[-1]
    print(last_item)
    last_value = int(last_item)

    print(begin_index)
    print(end_index)



    while begin_index <= end_index:
        # item é o 2009
        print(item)
        # 25
        print(end_index)
        if item > last_value :
             print("Number is over the end index!")
             break
        if item < begin_index:
             print("Number too small!")
             break


        """Aqui ele "corta" e cria o midpoint"""
        midpoint = begin_index + (end_index - begin_index) // 2
        """Aqui ele pega no midpoint criado e mete na variavel midpoint_value"""
        midpoint_string = sequence[midpoint]
        """Conversão de midpoint_value de string para int porque nao da para comparar strings com ints """
        midpoint_value = int(midpoint_string)


        print(f"Midpoint  is...", midpoint_value)
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
            print(f"Changing begin index...", begin_index)

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
            

