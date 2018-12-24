import json

def templateSearcher():

    print("Please enter the name of the JSON file you wish to search. CTRL+C to Quit.\n")
    jsonReader = input()

    print("Please select a template from below")
    print("1: Drug related crime")
    print("2: Violent Crime")
    print("3: Vehicular Crime")
    print("4: Criminal Damage")
    print("5: Fraudulent Crime")

    choice = input("Enter your choice: ")
    if choice == "1":
        value = ["drugs","drug","intent to supply","cannabis","cocaine","heroin","LSD","ketamine","amphetamine"]
    elif choice == "2":
        value = ["violence","stabbing","knife attack","assault","sexual assault","mugging","firearm","killed"]
    elif choice == "3":
        value = ["drink driving","dangerous driving","crash","speeding"]
    elif choice == "4":
        value = ["vandalism","vandalised","graffiti","damaged","arson"]
    elif choice == "5":
        value = ["fraud","identity theft","stolen","credit card","debit card","fraudulent"]
    else:
        print("You didn't select a valid option, please select a valid option.")

    #crimeChoice()

    with open(jsonReader, encoding="utf-8") as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            for word in value:
                if word in tempText:
                    countt = countt + 1
                    StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + " Tweet Text:" + data['text']
                    print(StringToScroll)