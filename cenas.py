palavras = ["abacaxi", "uva", "banana", "laranja"]

        for i in range(len(title)):
            for j in range(0, len(title) - i - 1):
                
                if title[j] > title[j + 1]:
                    
                    title[j], title[j + 1] = title[j + 1], title[j]
        print(title)