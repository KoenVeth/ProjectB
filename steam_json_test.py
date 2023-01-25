import json
import operator

game = input("choose your game (make sure its spelled correctly): ")  # choose the game
j = open("steam.json")  # open json
data = json.load(j)  # load the data
data.sort(key=operator.itemgetter('name'))  # sort the games by name


def binary_search_algorithm(data, min, max, game):
    if max >= min:
        mid = (max + min) // 2
        if data[mid]["name"] == game:
            return mid
        elif data[mid]["name"] > game:
            return binary_search_algorithm(data, min, mid - 1, game)
        else:
            return binary_search_algorithm(data, mid + 1, max, game)
    else:
        return -1


result = binary_search_algorithm(data, 0, len(data) - 1, game)


if result != -1:
    appid = data[result]["appid"]
    name = data[result]["name"]
    release_date = data[result]["release_date"]
    english = data[result]["english"]
    if english == 0:
        english = "No"
    else:
        english = "Yes"
    developer = data[result]["developer"]
    publisher = data[result]["publisher"]
    platforms = data[result]["platforms"]
    required_age = data[result]["required_age"]
    categories = data[result]["categories"]
    genres = data[result]["genres"]
    steamspy_tags = data[result]['steamspy_tags']
    achievements = data[result]['achievements']
    postive_ratings = data[result]['positive_ratings']
    negative_ratings = data[result]['negative_ratings']
    average_playtime = data[result]['average_playtime']
    median_playtime = data[result]['median_playtime']
    owners = data[result]['owners']
    price = data[result]['price']
    print(appid, name, release_date, english, developer, publisher, platforms, required_age, categories,
          genres, steamspy_tags, achievements, postive_ratings, negative_ratings, average_playtime, median_playtime,
          owners, price)
else:
    print("Error, game not found! Check your spelling and try again")
