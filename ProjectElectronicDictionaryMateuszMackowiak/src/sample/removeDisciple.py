def removeDisciple(language):
    import json
    from menu import menu
    from displayAllDisciples import displayAllDisciples
    if(language=="EN"):
        print("You entered process of removing disciple. Choose disciple by typing in his Id from list below.")
        displayAllDisciples(language)
        choose = str(input())
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
        with open('../../data/data.txt', 'w') as outfile:
            del data['disciples'][int(choose)]
            number = 0  # reassigning id after deletion
            for i in data['disciples']:
                i['id'] = str(number)
                number = number + 1
            json.dump(data, outfile)
        return menu(language)
    if (language == "PL"):
        print("Weszles w proces usuwania ucznia. Wybierz ucznia poprzez wpisanie jego Id z listy ponizej,")
        displayAllDisciples(language)
        choose = str(input())
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
        with open('../../data/data.txt', 'w') as outfile:
            del data['disciples'][int(choose)]
            number=0#reassigning id after deletion
            for i in data['disciples']:
                i['id']=str(number)
                number=number+1
            json.dump(data, outfile)
        return menu(language)