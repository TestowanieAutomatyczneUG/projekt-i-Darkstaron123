def addMark(language,discipleId,subjectId):
    import json
    from editSubject import editSubject
    if (language == "EN"):
        print("You entered process of adding mark. Type in mark you want to add.")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            print("Marks:")
            print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
            choose = str(input())
        with open('../../data/data.txt', 'w') as outfile:
            data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].append(str(choose))
            json.dump(data, outfile)
        return editSubject(language, discipleId)
    if (language == "PL"):
        print("Weszles w proces usuwania ucznia. Wybierz ucznia poprzez wpisanie jego Id z listy ponizej,")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            print("Marks:")
            print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
            choose = str(input())
        with open('../../data/data.txt', 'w') as outfile:
            data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].append(str(choose))
            json.dump(data, outfile)
        return editSubject(language, discipleId)