import json

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


