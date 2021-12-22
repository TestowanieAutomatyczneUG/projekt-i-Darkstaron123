def removeMark(language,discipleId,subjectId):
    import json
    from editSubject import editSubject
    if (language == "EN"):
        print("You entered process of removing mark. Type in mark you want to remove.")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            print("Marks:")
            print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
            choose = str(input())
        with open('../../data/data.txt', 'w') as outfile:
            for i in data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks']:
                if(str(i)==str(choose)):
                    data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].remove(i)
                    break
            json.dump(data, outfile)
        return editSubject(language,discipleId)
    if (language == "PL"):
        print("Weszles w proces usuwania ucznia. Wybierz ucznia poprzez wpisanie jego Id z listy ponizej,")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            print("Oceny:")
            print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
            choose = str(input())
        with open('../../data/data.txt', 'w') as outfile:
            for i in data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks']:
                if (i == choose):
                    data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].remove(i)
                    break
            json.dump(data, outfile)
        return editSubject(language, discipleId)