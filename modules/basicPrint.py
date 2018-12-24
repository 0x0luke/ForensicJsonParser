import json

def basicPrint(): # basic print module
    print("Please enter the name of the JSON file you wish to parse. CTRL+C to Quit.\n")
    jsonReader = input()
    count = 0
    with open(jsonReader, encoding='utf-8') as data_file:
        for row in data_file:
            data = json.loads(row)
            count = count+1
            try:
                print("Created at: "+data['createdAt']['$date'])
                print("Latitude: " +str(data['geoLocation']['latitude']))
                print("Longitude: " + str(data['geoLocation']['longitude']))
                print("Tweet text: "+data['text'])
                print("Place Name: "+data['place']['name'])
                print("Place full name: "+data['place']['fullName']+"\n")
                print("..... Next Record .....\n")
            except KeyError:
                print("Data error, moving on..")

        print("Printed "+str(count)+" Records succesfully")