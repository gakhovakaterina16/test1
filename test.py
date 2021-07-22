import requests
import hashlib
import time
from selenium import webdriver

url = "https://line11.bkfon-resources.com/live/currentLine/ru"
response = requests.get(url)
data = response.json()

parentId_football = []
leagueId_football = []
for element in data["sports"]:
    if element["name"] == "Футбол" and element["kind"] == "sport":
        parentId_football.append(element["id"])

for element in data["sports"]:
    if element["kind"] == "segment" and element["parentId"] in parentId_football:
        leagueId_football.append(element["id"])

for element in data["events"]:
    if element["level"] == 1 and element["sportId"] in leagueId_football:
        hash_id = hashlib.md5(str(element["id"]).encode("utf-8"))
        gamers = {hash_id: f"gamer_name = {element['team1']} - {element['team2']}"}  

print(gamers)

game_to_find = list(gamers.values())[0].replace("gamer_name = ", "")


driver = webdriver.Chrome()
driver.get("https://google.ru")
element = driver.find_element_by_name("q")
element.send_keys(f"{game_to_find}\n")

print(game_to_find)
