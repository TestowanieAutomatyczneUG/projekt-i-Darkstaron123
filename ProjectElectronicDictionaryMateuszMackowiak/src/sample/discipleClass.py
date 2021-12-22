class DiscipleClass:
    def displayAllDisciples(language):
        import json
        if (language == "EN"):
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                for i in data['disciples']:
                    print('Id: ' + i['id'], end=" ")
                    print('First Name: ' + i['firstname'], end=" ")
                    print('Last Name: ' + i['lastname'], end=" ")
                    print('')
        if (language == "PL"):
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                for i in data['disciples']:
                    print('Id: ' + i['id'], end=" ")
                    print('Pierwsze Imie: ' + i['firstname'], end=" ")
                    print('Nazwisko: ' + i['lastname'], end=" ")
                    print('')

    def chooseAndDisplayDisciple(language):
        import json
        from discipleClass import DiscipleClass
        from menuClass import MenuClass
        if (language == "EN"):
            print("Choose disciple by typing in his Id from list below.")
            DiscipleClass.displayAllDisciples(language)
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
            return MenuClass.menu(language)
        if (language == "PL"):
            print("Wybierz ucznia poprzez wpisanie jego Id z listy ponizej.")
            DiscipleClass.displayAllDisciples(language)
            choose = str(input())
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                # print(data['disciples'][int(choose)])
                print("Id:" + data['disciples'][int(choose)]['id'])
                print("Pierwsze Imie:" + data['disciples'][int(choose)]['firstname'])
                print("Nazwisko:" + data['disciples'][int(choose)]['lastname'])
                print("Przedmioty:")
                for i in data['disciples'][int(choose)]['subjects']:
                    print(' ' + i['name'])
                    print(' Oceny:')
                    for ii in i['marks']:
                        print('  ' + ii, end=", ")
                    print('')
            print("Wprowadz cokolwiek zeby wrocic do menu.")
            input()
            return MenuClass.menu(language)

    def addDisciple(language):
        import json
        from menuClass import MenuClass
        if (language == "EN"):
            print("You entered process of adding disciple.")
            print("Type in his first name.")
            firstname = str(input())
            print("Type in his last name.")
            lastname = str(input())
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
            with open('../../data/data.txt', 'w') as outfile:
                data['disciples'].append(
                    {
                        "id": str(len(data['disciples'])),
                        "firstname": firstname,
                        "lastname": lastname,
                        "subjects": []
                    }
                )
                json.dump(data, outfile)
            return MenuClass.menu(language)
        if (language == "PL"):
            print("Weszles w proces dodawania ucznia.")
            print("Wpisz jego pierwsze imie.")
            firstname = str(input())
            print("Wpisz jego nazwisko.")
            lastname = str(input())
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
            with open('../../data/data.txt', 'w') as outfile:
                data['disciples'].append(
                    {
                        "id": str(len(data['disciples'])),
                        "firstname": firstname,
                        "lastname": lastname,
                        "subjects": []
                    }
                )
                json.dump(data, outfile)
            return MenuClass.menu(language)
    def editDisciple(language):
        import json
        from menuClass import MenuClass
        from discipleClass import DiscipleClass
        from subjectClass import SubjectClass
        if (language == "EN"):
            print("You entered process of editing disciple. Choose disciple by typing in his Id from list below.")
            DiscipleClass.displayAllDisciples(language)
            choose = str(input())
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                disciple = data['disciples'][int(choose)]
                print("=>Choosen disciple.<=")
                print("Id:" + disciple['id'])
                print("First Name:" + disciple['firstname'])
                print("Last Name:" + disciple['lastname'])
                print("Subjects:")
                for i in disciple['subjects']:
                    print(' ' + i['name'])
                    print(' Marks:')
                    for ii in i['marks']:
                        print('  ' + ii, end=", ")
                    print('')
                print('Pick an option.')
                print("0. Go back to menu.")
                print("1. Type in disciple\'s new first name.")
                print("2. Type in disciple\'s new last name.")
                print("3. Add subject to disciple.")
                print("4. Edit disciple\'s subject.")
                print("5. Remove disciple\'s subject.")
                choose = str(input())
                if (choose == "0"):
                    return MenuClass.menu(language)
                elif (choose == "1"):
                    disciple['firstname'] = str(input())
                elif (choose == "2"):
                    disciple['lastname'] = str(input())
                elif (choose == "3"):
                    SubjectClass.addSubject(language, disciple['id'])
                elif (choose == "4"):
                    SubjectClass.editSubject(language, disciple['id'])
                elif (choose == "5"):
                    SubjectClass.removeSubject(language, disciple['id'])
                else:
                    print('You had a typo. Try again!')
                    return DiscipleClass.editDisciple(language)

            with open('../../data/data.txt', 'w') as outfile:
                data['disciples'][int(disciple['id'])] = disciple
                json.dump(data, outfile)
            return DiscipleClass.editDisciple(language)
        if (language == "PL"):
            print("Weszles w proces edytowania ucznia. Wybierz ucznia poprzez wpisanie jego Id z listy ponizej.")
            DiscipleClass.displayAllDisciples(language)
            choose = str(input())
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                disciple = data['disciples'][int(choose)]
                print("=>Wybrany uczen.<=")
                print("Id:" + disciple['id'])
                print("Imie:" + disciple['firstname'])
                print("Nazwisko:" + disciple['lastname'])
                print("Przedmioty:")
                for i in disciple['subjects']:
                    print(' ' + i['name'])
                    print(' Oceny:')
                    for ii in i['marks']:
                        print('  ' + ii, end=", ")
                    print('')
                print('Wybierz opcje.')
                print("0. Wroc do menu.")
                print("1. Wpisz nowe imie dla wybranego ucznia.")
                print("2. Wpisz nowe nazwisko dla wybranego ucznia.")
                print("3. Dodaj przedmiot do wybranego ucznia.")
                print("4. Edytuj przedmiot wybranego ucznia.")
                print("5. Usun przedmiot wybranego ucznia.")
                choose = str(input())
                if (choose == "0"):
                    return MenuClass.menu(language)
                elif (choose == "1"):
                    disciple['firstname'] = str(input())
                elif (choose == "2"):
                    disciple['lastname'] = str(input())
                elif (choose == "3"):
                    SubjectClass.addSubject(language, disciple['id'])
                elif (choose == "4"):
                    SubjectClass.editSubject(language, disciple['id'])
                elif (choose == "5"):
                    SubjectClass.removeSubject(language, disciple['id'])
                else:
                    print('Miales literowke. Sproboj ponownie!')
                    return DiscipleClass.editDisciple(language)

            with open('../../data/data.txt', 'w') as outfile:
                data['disciples'][int(disciple['id'])] = disciple
                json.dump(data, outfile)
            return DiscipleClass.editDisciple(language)

    def removeDisciple(language):
        import json
        from menuClass import MenuClass
        from discipleClass import DiscipleClass
        if (language == "EN"):
            print("You entered process of removing disciple. Choose disciple by typing in his Id from list below.")
            DiscipleClass.displayAllDisciples(language)
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
            return MenuClass.menu(language)
        if (language == "PL"):
            print("Weszles w proces usuwania ucznia. Wybierz ucznia poprzez wpisanie jego Id z listy ponizej,")
            DiscipleClass.displayAllDisciples(language)
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
            return MenuClass.menu(language)
