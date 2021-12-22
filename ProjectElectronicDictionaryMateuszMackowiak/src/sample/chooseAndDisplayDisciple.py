def chooseAndDisplayDisciple(language):
    import json
    from menu import menu
    from displayAllDisciples import displayAllDisciples
    if(language=="EN"):
        print("Choose disciple by typing in his Id from list below.")
        displayAllDisciples(language)
        choose = str(input())
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            # print(data['disciples'][int(choose)])
            print("Id:" + data['disciples'][int(choose)]['id'])
            print("First Name:" + data['disciples'][int(choose)]['firstname'])
            print("Last Name:" + data['disciples'][int(choose)]['lastname'])
            print("Subjects:")
            for i in data['disciples'][int(choose)]['subjects']:
                print(' ' + i['name'])
                print(' Marks:')
                for ii in i['marks']:
                    print('  ' + ii, end=", ")
                print('')
        print("Type in anything to return to menu")
        input()
        return menu(language)
    if(language=="PL"):
        print("Wybierz ucznia poprzez wpisanie jego Id z listy ponizej.")
        displayAllDisciples(language)
        choose = str(input())
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            #print(data['disciples'][int(choose)])
            print("Id:" + data['disciples'][int(choose)]['id'])
            print("Pierwsze Imie:" + data['disciples'][int(choose)]['firstname'])
            print("Nazwisko:" + data['disciples'][int(choose)]['lastname'])
            print("Przedmioty:")
            for i in data['disciples'][int(choose)]['subjects']:
                print(' '+i['name'])
                print(' Oceny:')
                for ii in i['marks']:
                    print('  '+ii,end=", ")
                print('')
        print("Wprowadz cokolwiek zeby wrocic do menu.")
        input()
        return menu(language)
