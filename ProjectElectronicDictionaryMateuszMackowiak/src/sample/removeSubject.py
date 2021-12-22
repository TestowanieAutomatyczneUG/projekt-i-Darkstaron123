def removeSubject(language,discipleId):
    import json
    from menu import menu
    from displayAllDisciples import displayAllDisciples
    if (language == "EN"):
        print("You entered process of removing subject. Choose subject by typing in his Id from list below.")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            for i in data['disciples'][int(discipleId)]['subjects']:
                print("Id: "+i['id']+" Name: "+i['name'])
        typedId = str(input())

        with open('../../data/data.txt', 'w') as outfile:
            del data['disciples'][int(discipleId)]['subjects'][int(typedId)]
            number = 0  # reassigning id after deletion
            for i in data['disciples'][int(discipleId)]['subjects']:
                i['id'] = str(number)
                number = number + 1
            json.dump(data, outfile)
        return menu(language)
    if (language == "PL"):
        print("Weszles w proces usuwania przedmiotu. Wybierz przedmiot poprzez wpisanie jego Id z listy ponizej,")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            for i in data['disciples'][int(discipleId)]['subjects']:
                print("Id: " + i['id'] + " Nazwa: " + i['name'])
        typedId = str(input())

        with open('../../data/data.txt', 'w') as outfile:
            del data['disciples'][int(discipleId)]['subjects'][int(typedId)]
            number = 0  # reassigning id after deletion
            for i in data['disciples'][int(discipleId)]['subjects']:
                i['id'] = str(number)
                number = number + 1
            json.dump(data, outfile)
        return menu(language)