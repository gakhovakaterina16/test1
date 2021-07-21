import requests
import hashlib
import time
from selenium import webdriver

url = "https://line11.bkfon-resources.com/live/currentLine/ru"
response = requests.get(url)
data = response.json()

football_sport_id = []
for element in data["sports"]:
    if "Футбол" in element["name"] and element["kind"] == "segment":
        football_sport_id.append(element["id"])


for event in data["events"]:
    if event["sportId"] in football_sport_id:
        if event["kind"] == 1:
            if event["place"] == "live":
                hash_id = hashlib.md5(str(event["id"]).encode("utf-8"))
                gamers = {hash_id: f"gamer_name = {event['team1']} - {event['team2']}"}

game_to_find = list(gamers.values())[0].replace("gamer_name = ", "")

driver = webdriver.Chrome()
driver.get("https://google.ru")
element = driver.find_element_by_name("q")
element.send_keys(f"{game_to_find}\n")

print(game_to_find)
