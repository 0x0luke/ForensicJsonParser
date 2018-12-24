import json

def jsonSearcher():

    print("Please enter your search query\n")
    searchQuery = input()
    print("Please enter the name of the JSON file you wish to search. CTRL+C to Quit.\n")
    jsonReader = input()
    with open(jsonReader, encoding="utf-8") as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']

           # print("you have entered ... "+tempText)
            
            if searchQuery in tempText:
                countt = countt + 1
                StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + " Tweet Text:" + data['text']
                print(StringToScroll)