import  json
ini = input("choose your game (make sure its spelled correctly): ")#choose the game
inp=0
print('loading.....')
while True:

    inp=inp+1
    if ini=="Counter-Strike":
        inp=0

    j = open("steam.json") #open json
    data = json.load(j) #load the data
    app_id = data[inp]['appid'] #save app_id
    name = data[inp]['name'] #save name
    release_date = data[inp]['release_date']# save release date
    english = data[inp]['english'] #saved whether the game is in english
    if english == 1:# if its 1 return yes
        english = "Yes"
    else:
        english = "No" #else return no
    developer = data[inp]['developer'] #save all  data
    publisher = data[inp]['publisher']
    platforms = data[inp]['platforms']
    required_age = data[inp]['required_age']
    categories = data[inp]['categories']
    genres = data[inp]['genres']
    steamspy_tags = data[inp]['steamspy_tags']
    achievements = data[inp]['achievements']
    postive_ratings = data[inp]['positive_ratings']
    negative_ratings = data[inp]['negative_ratings']
    average_playtime = data[inp]['average_playtime']
    median_playtime = data[inp]['median_playtime']
    owners = data[inp]['owners']
    price = data[inp]['price']
    if price == 0:    #if price =0 return free
        price ='Free'
        #remove hashtags to show search process
    #print(app_id, name, release_date, english, developer, publisher, platforms, required_age, categories,
         # genres, steamspy_tags, achievements, postive_ratings, negative_ratings, average_playtime, median_playtime,
          #owners, price)
    if inp>=0:
        inp=inp+1
        inp=inp//-1

    else:
        inp=inp//-1

    if ini==name:
        print(app_id, name, release_date, english, developer, publisher, platforms, required_age, categories,
              genres, steamspy_tags, achievements, postive_ratings, negative_ratings, average_playtime, median_playtime,
              owners, price)
        break

     #print to test

    j.close() #close json