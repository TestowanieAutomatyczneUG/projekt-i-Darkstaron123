def menu(language):
    from chooseAndDisplayDisciple import chooseAndDisplayDisciple
    from addDisciple import addDisciple
    from removeDisciple import removeDisciple
    from editDisciple import editDisciple
    if(language=='PL'):
        print('Czesc, zalogowales sie do dziennika. Wybierz opcje, poprzez wpisanie jej numeru:')
        print('0. Wybierz i wyswietl ucznia.')
        print('1. Dodanie ucznia.')
        print('2. Edycja ucznia.')
        print('3. Usuniecie ucznia.')
        print('4. Wyloguj sie.')
        choose=str(input())
        if(choose=="0"):
            chooseAndDisplayDisciple(language)
        elif(choose=="1"):
            addDisciple(language)
        elif (choose == "2"):
            editDisciple(language)
        elif (choose == "3"):
            removeDisciple(language)
        elif (choose == "4"):
            print("Wylogowales sie!")
            return 0
    elif(language=='EN'):
        print('Hello, you logged in electronic dictionary. Choose option, by typing in it\'s number:')
        print('0. Choose and show disciple')
        print('1. Add disciple')
        print('2. Edit disciple')
        print('3. Delete disciple')
        print('4. Log Out')
        choose = str(input())
        if (choose == "0"):
            chooseAndDisplayDisciple(language)
        elif (choose == "1"):
            addDisciple(language)
        elif (choose == "2"):
            editDisciple(language)
        elif (choose == "3"):
            removeDisciple(language)
        elif (choose == "4"):
            print("You have logged out!")
            return 0
    else:
        print('You had a typo. Try again!')
        print('Miales literowke. Sproboj jeszcze raz!')
        return menu(language)
