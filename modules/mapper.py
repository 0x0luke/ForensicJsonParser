import json
import webbrowser
try:
    import folium
except ImportError:
    raise ImportError('I cannot find the folium module! Is it installed?')

def Mapper():
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    print("Please enter the name of the JSON file you wish to map. CTRL+C to Quit.\n")
    jsonReader = input()
    print("Please enter a search Query")
    searchQuery = input()
    
    print("Doing it.")
    with open(jsonReader, encoding="utf-8") as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']
            tempText = data['text']

            if searchQuery in tempText:
                countt = countt + 1
                folium.Marker([latt,longg], popup=tempText.replace('\'', '')).add_to(map_osm) ##some of the tweets have apostrophes in, which will cause javascript errors when the map is exported, this removes the apostrophes

    map_osm.save(searchQuery+'.html')
    webbrowser.open(searchQuery+'.html') #opens the results