import  json
inp=int(input("choose game ")) #choose the game
j=open("steam.json") #open json
data=json.load(j) #load the data
app_id=data[inp]['appid'] #save app_id
name=data[inp]['name'] #save name
release_date=data[inp]['release_date']# save release date
print(app_id,name,release_date) #print to test

j.close()