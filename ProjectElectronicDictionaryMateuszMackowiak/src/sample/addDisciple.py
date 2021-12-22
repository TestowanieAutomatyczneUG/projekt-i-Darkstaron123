def addDisciple(language):
    import json
    from menu import menu
    if(language=="EN"):
        print("You entered process of adding disciple.")
        print("Type in his first name.")
        firstname=str(input())
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
        return menu(language)
    if(language=="PL"):
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
        return menu(language)