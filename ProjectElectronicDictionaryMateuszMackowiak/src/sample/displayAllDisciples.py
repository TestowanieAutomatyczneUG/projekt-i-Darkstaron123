def displayAllDisciples(language):
    import json
    if (language == "EN"):
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            for i in data['disciples']:
                print('Id: ' + i['id'],end=" ")
                print('First Name: ' + i['firstname'],end=" ")
                print('Last Name: ' + i['lastname'],end=" ")
                print('')
    if (language == "PL"):
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            for i in data['disciples']:
                print('Id: ' + i['id'],end=" ")
                print('Pierwsze Imie: ' + i['firstname'],end=" ")
                print('Nazwisko: ' + i['lastname'],end=" ")
                print('')