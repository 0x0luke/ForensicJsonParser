import json
import re

def regexSearcher():

    print("Please enter the name of the JSON file you wish to search. CTRL+C to Quit.\n")
    jsonReader = input()

    print("Please enter a Regular Expression")
    regexInput = input()

    regex = re.compile(regexInput)

    with open(jsonReader, encoding="utf-8") as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            result = regex.findall(data['text'])
            if result:
                for res in result:
                    countt = countt + 1
                    StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + " Tweet Text:" + data['text']
                    print(StringToScroll)