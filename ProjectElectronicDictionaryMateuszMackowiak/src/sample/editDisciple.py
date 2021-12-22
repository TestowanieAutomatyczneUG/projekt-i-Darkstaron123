def editDisciple(language):
    import json
    from menu import menu
    from displayAllDisciples import displayAllDisciples
    from addSubject import addSubject
    from editSubject import editSubject
    from removeSubject import removeSubject
    if (language == "EN"):
        print("You entered process of editing disciple. Choose disciple by typing in his Id from list below.")
        displayAllDisciples(language)
        choose = str(input())
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            disciple=data['disciples'][int(choose)]
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
            choose=str(input())
            if(choose == "0"):
                return menu(language)
            elif (choose == "1"):
                disciple['firstname'] = str(input())
            elif (choose == "2"):
                disciple['lastname'] = str(input())
            elif (choose == "3"):
                addSubject(language,disciple['id'])
            elif (choose == "4"):
                editSubject(language,disciple['id'])
            elif (choose == "5"):
                removeSubject(language,disciple['id'])
            else:
                print('You had a typo. Try again!')
                return editDisciple(language)

        with open('../../data/data.txt', 'w') as outfile:
            data['disciples'][int(disciple['id'])]=disciple
            json.dump(data, outfile)
        return editDisciple(language)
    if (language == "PL"):
        print("Weszles w proces edytowania ucznia. Wybierz ucznia poprzez wpisanie jego Id z listy ponizej.")
        displayAllDisciples(language)
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
                return menu(language)
            elif (choose == "1"):
                disciple['firstname'] = str(input())
            elif (choose == "2"):
                disciple['lastname'] = str(input())
            elif (choose == "3"):
                addSubject(language,disciple['id'])
            elif (choose == "4"):
                pass
            elif (choose == "5"):
                pass
            else:
                print('Miales literowke. Sproboj ponownie!')
                return editDisciple(language)

        with open('../../data/data.txt', 'w') as outfile:
            data['disciples'][int(disciple['id'])]=disciple
            json.dump(data, outfile)
        return editDisciple(language)