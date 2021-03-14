import requests
import json

#URL is the GET javascript call from the site which returns JSON.
#house = realm AH id, item = item id
#the price will look something like this 89500 (8g 95s 00c)
URL = "https://theunderminejournal.com/api/item.php?house=110&item=171828"
page = requests.get(URL)
item_json_data = json.loads(page.content)
item_price = item_json_data["stats"][0]["price"] / 10000

#URL is the Get javascript call which returns a JSON containing the unix time
URL = "https://theunderminejournal.com/api/house.php?house=110"
page = requests.get(URL)
date_json_data = json.loads(page.content)
last_updated = date_json_data["timestamps"]["lastupdate"]
next_update = date_json_data["timestamps"]["scheduled"]

#this value gets returned to the main process which will be used to determine the price and next time to scan
returnValue = {"current_price" : item_price, "last_updated" : last_updated, "next_update" : next_update}
print(returnValue)