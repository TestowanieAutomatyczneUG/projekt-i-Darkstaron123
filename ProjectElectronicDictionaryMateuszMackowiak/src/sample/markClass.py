class MarkClass:
    def addMark(language, discipleId, subjectId):
        import json
        from subjectClass import SubjectClass
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
            return SubjectClass.editSubject(language, discipleId)
        if (language == "PL"):
            print("Weszles w proces usuwania ucznia. Wybierz ucznia poprzez wpisanie jego Id z listy ponizej,")
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                print("Oceny:")
                print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
                choose = str(input())
            with open('../../data/data.txt', 'w') as outfile:
                data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].append(str(choose))
                json.dump(data, outfile)
            return SubjectClass.editSubject(language, discipleId)

    def editMark(language, discipleId, subjectId):
        import json
        from subjectClass import SubjectClass
        if (language == "EN"):
            print("You entered process of editing mark. Type in mark you want to edit.")
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                print("Marks:")
                print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
                choose = str(input())
                print("Type in new mark.")
                newmark = str(input())
            with open('../../data/data.txt', 'w') as outfile:
                for i in data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks']:
                    if (str(i) == str(choose)):
                        data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].remove(i)
                        data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].append(newmark)
                        break
                json.dump(data, outfile)
            return SubjectClass.editSubject(language, discipleId)
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
            return SubjectClass.editSubject(language, discipleId)

    def removeMark(language, discipleId, subjectId):
        import json
        from subjectClass import SubjectClass
        if (language == "EN"):
            print("You entered process of removing mark. Type in mark you want to remove.")
            with open('../../data/data.txt') as json_file:
                data = json.load(json_file)
                print("Marks:")
                print(data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'])
                choose = str(input())
            with open('../../data/data.txt', 'w') as outfile:
                for i in data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks']:
                    if (str(i) == str(choose)):
                        data['disciples'][int(discipleId)]['subjects'][int(subjectId)]['marks'].remove(i)
                        break
                json.dump(data, outfile)
            return SubjectClass.editSubject(language, discipleId)
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
            return SubjectClass.editSubject(language, discipleId)