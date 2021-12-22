class SubjectClass:
    def addSubject(language, discipleId):
        import json
        from editDisciple import editDisciple
        if (language == "EN"):
            print("You entered process of adding subject to disciple.")
            print("Type in new subject\'s name.")
            name = str(input())
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
            with open('../../data/data.txt', 'w') as outfile:
                data['disciples'][int(discipleId)]['subjects'].append(
                    {
                        "id": str(len(data['disciples'][int(discipleId)]['subjects'])),
                        "name": name,
                        "marks": []
                    }
                )
                json.dump(data, outfile)
            return editDisciple(language)
        if (language == "PL"):
            print("Weszles w proces dodawania przedmiotu do ucznia")
            print("Wpisz nazwe nowego przedmiotu.")
            name = str(input())
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
            with open('../../data/data.txt', 'w') as outfile:
                data['disciples'][int(discipleId)]['subjects'].append(
                    {
                        "id": str(len(data['disciples'][int(discipleId)]['subjects'])),
                        "name": name,
                        "marks": []
                    }
                )
                json.dump(data, outfile)
            return editDisciple(language)

    def editSubject(language, discipleId):
        import json
        from menu import menu
        from discipleClass import DiscipleClass
        from editDisciple import editDisciple
        from addMark import addMark
        from removeMark import removeMark
        from editMark import editMark
        if (language == "EN"):
            print("You entered process of editing subject of disciple.")
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
            print("List of subjects of this disciple.")
            for i in data['disciples'][int(discipleId)]['subjects']:
                print("Id: " + i['id'] + " Name: " + i['name'])
            print("Choose subject to edit by typing in it\'s id.")
            typedId = str(input())
            print("=>Choosen subject.<=")
            print("Name: " + data['disciples'][int(discipleId)]['subjects'][int(typedId)]['name'])
            print("Marks: ", end="")
            for i in data['disciples'][int(discipleId)]['subjects'][int(typedId)]['marks']:
                print(i, end=" ")
            print()
            print('Pick an option.')
            print("0. Go back to menu of editing disciple.")
            print("1. Type in disciple\'s subject new name.")
            print("2. Add mark to disciple\'s subject.")
            print("3. Edit disciple\'s mark.")
            print("4. Remove disciple\'s mark.")
            choose = str(input())
            if (choose == "0"):
                return DiscipleClass.editDisciple(language)
            elif (choose == "1"):
                data['disciples'][int(discipleId)]['subjects'][int(typedId)]['name'] = str(input())
            elif (choose == "2"):
                addMark(language, discipleId, typedId)
            elif (choose == "3"):
                editMark(language, discipleId, typedId)
            elif (choose == "4"):
                removeMark(language, discipleId, typedId)
            else:
                print('You had a typo. Try again!')
                return editSubject(language, discipleId)
            with open('../../data/data.txt', 'w') as outfile:
                json.dump(data, outfile)
            return editDisciple(language)
        if (language == "PL"):
            print("Weszles w proces edytowania przedmiotu ucznia.")
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
            print("Lista przedmiotow wybranego ucznia.")
            for i in data['disciples'][int(discipleId)]['subjects']:
                print("Id: " + i['id'] + " Name: " + i['name'])
            print("Wybierz przedmiot to zedytowania poprzez wpisanie jego id.")
            typedId = str(input())
            print("=>Wybrany przedmiot.<=")
            print("Nazwa: " + data['disciples'][int(discipleId)]['subjects'][int(typedId)]['name'])
            print("Oceny: ", end="")
            for i in data['disciples'][int(discipleId)]['subjects'][int(typedId)]['marks']:
                print(i, end=" ")
            print()
            print('Wybierz opcje.')
            print("0. Wroc do menu edytowania ucznia.")
            print("1. Wpisz nowa nazwe dla wybranego przedmiotu.")
            print("2. Dodaj ocene do wybranego przedmiotu.")
            print("3. Zedytuj ocene w wybranym przedmiocie.")
            print("4. Usun ocene w wybranym przedmiocie.")
            choose = str(input())
            if (choose == "0"):
                return DiscipleClass.editDisciple(language)
            elif (choose == "1"):
                data['disciples'][int(discipleId)]['subjects'][int(typedId)]['name'] = str(input())
            elif (choose == "2"):
                addMark(language, discipleId, typedId)
            elif (choose == "3"):
                editMark(language, discipleId, typedId)
            elif (choose == "4"):
                removeMark(language, discipleId, typedId)
            else:
                print('Miales literowke. Sproboj ponownie!')
                return editSubject(language, discipleId)
            with open('../../data/data.txt', 'w') as outfile:
                json.dump(data, outfile)
            return editDisciple(language)

    def removeSubject(language, discipleId):
        import json
        from menuClass import MenuClass
        if (language == "EN"):
            print("You entered process of removing subject. Choose subject by typing in his Id from list below.")
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                for i in data['disciples'][int(discipleId)]['subjects']:
                    print("Id: " + i['id'] + " Name: " + i['name'])
            typedId = str(input())

            with open('../../data/data.txt', 'w') as outfile:
                del data['disciples'][int(discipleId)]['subjects'][int(typedId)]
                number = 0  # reassigning id after deletion
                for i in data['disciples'][int(discipleId)]['subjects']:
                    i['id'] = str(number)
                    number = number + 1
                json.dump(data, outfile)
            return MenuClass.menu(language)
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
            return MenuClass.menu(language)