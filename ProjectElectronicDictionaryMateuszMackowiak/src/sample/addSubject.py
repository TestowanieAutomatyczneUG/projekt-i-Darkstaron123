def addSubject(language,discipleId):
    import json
    from menu import menu
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
                    "id":str(len(data['disciples'][int(discipleId)]['subjects'])),
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