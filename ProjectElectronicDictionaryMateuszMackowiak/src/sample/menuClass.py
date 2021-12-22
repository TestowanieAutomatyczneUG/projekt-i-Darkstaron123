class MenuClass:
    def menu(language):
        from discipleClass import DiscipleClass
        if (language == 'PL'):
            print('Czesc, zalogowales sie do dziennika. Wybierz opcje, poprzez wpisanie jej numeru:')
            print('0. Wybierz i wyswietl ucznia.')
            print('1. Dodanie ucznia.')
            print('2. Edycja ucznia.')
            print('3. Usuniecie ucznia.')
            print('4. Wyloguj sie.')
            choose = str(input())
            if (choose == "0"):
                DiscipleClass.chooseAndDisplayDisciple(language)
            elif (choose == "1"):
                DiscipleClass.addDisciple(language)
            elif (choose == "2"):
                DiscipleClass.editDisciple(language)
            elif (choose == "3"):
                DiscipleClass.removeDisciple(language)
            elif (choose == "4"):
                print("Wylogowales sie!")
                return 0
        elif (language == 'EN'):
            print('Hello, you logged in electronic dictionary. Choose option, by typing in it\'s number:')
            print('0. Choose and show disciple')
            print('1. Add disciple')
            print('2. Edit disciple')
            print('3. Delete disciple')
            print('4. Log Out')
            choose = str(input())
            if (choose == "0"):
                DiscipleClass.chooseAndDisplayDisciple(language)
            elif (choose == "1"):
                DiscipleClass.addDisciple(language)
            elif (choose == "2"):
                DiscipleClass.editDisciple(language)
            elif (choose == "3"):
                DiscipleClass.removeDisciple(language)
            elif (choose == "4"):
                print("You have logged out!")
                return 0
        else:
            print('You had a typo. Try again!')
            print('Miales literowke. Sproboj jeszcze raz!')
            return menu(language)

    def chooseLanguage():
        print('To choose english language, type in: EN')
        print('Zeby wybrac polski jezyk, wpisz: PL')
        choose = str(input())
        language = choose
        return language