import json, operator #importeer 2 ingebouwde fucties van python


Bestand=open('steam.json')# open de steam json file en zet in variabele
data = json.load(Bestand)# laad bestand dus de json file die open is in data
data.sort(key=operator.itemgetter('appid'))# sorteer de data aan de hand van de opgegeven key die het eruit moet pakken
print(json.dumps(data, indent=2)) # print de gesorteerde json file die gesorteerd is op appid