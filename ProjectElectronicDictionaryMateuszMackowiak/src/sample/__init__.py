def main():
    from menu import menu
    from chooseLanguage import chooseLanguage

    menu(chooseLanguage())
main()#uruchomienie dziennika elektronicznego/starting electronic dictionary

    #import json
    #"""Entry point for the application script"""
    #print("Call your main application code here")

#    data = {}
#    data['people'] = []
#    data['people'].append({
#        'name': 'Scott',
#        'website': 'stackabuse.com',
#        'from': 'Nebraska'
#    })
#    data['people'].append({
#        'name': 'Larry',
#        'website': 'google.com',
#        'from': 'Michigan'
#    })
#    data['people'].append({
#        'name': 'Tim',
#        'website': 'apple.com',
#        'from': 'Alabama'
#    })
#    print(data)
#    with open('../../data/data.txt', 'w') as outfile:
#        json.dump(data, outfile)