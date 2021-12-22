def editMark(language,discipleId,subjectId):
    import json
    from editSubject import editSubject
    if (language == "EN"):
        print("You entered process of editing mark. Type in mark you want to edit.")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            print("Marks:")
            print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
            choose = str(input())
            print("Type in new mark.")
            newmark=str(input())
        with open('../../data/data.txt', 'w') as outfile:
            for i in data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks']:
                if (str(i) == str(choose)):
                    data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].remove(i)
                    data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].append(newmark)
                    break
            json.dump(data, outfile)
        return editSubject(language, discipleId)
    if (language == "PL"):
        print("Weszles w proces usuwania oceny. Wybierz ocene poprzez wpisanie jej listy ponizej,")
        with open('../../data/data.txt') as json_file:
            data = json.load(json_file)
            print("Oceny:")
            print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
            choose = str(input())
            print("Wpisz nowa ocene.")
            newmark = str(input())
        with open('../../data/data.txt', 'w') as outfile:
            for i in data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks']:
                if (str(i) == str(choose)):
                    data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].remove(i)
                    data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].append(newmark)
                    break
            json.dump(data, outfile)
        return editSubject(language, discipleId)