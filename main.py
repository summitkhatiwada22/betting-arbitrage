import requests
import json

url = "https://odds.p.rapidapi.com/v4/sports"


# LIST ALL SPORTS

querystring = {"all":"true"}

headers = {
	"X-RapidAPI-Key": "c5c0ac69f8mshea7d5d2e3bcc9e2p1b38bejsn978ca814bd1a",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
writeFile = open('all_sports.json', 'w+')
writeFile.write(response.text)
writeFile.close()

"""
RESPONSE FORMAT
 {
    "key": "americanfootball_cfl",
    "group": "American Football",
    "title": "CFL",
    "description": "Canadian Football League",
    "active": false,
    "has_outrights": false
}
"""

# EXTRACT ALL KEYS NAME
open_all_sports = open('all_sports.json')
all_sports_data = json.load(open_all_sports)

# array to hold the key of all sports available
all_sports_key = []

# counting and loopong through all the json objects
i = 0
while i < len(all_sports_data):
    # LOADING ALL SPORTS KEY IN A LIST
    all_sports_key.append(all_sports_data[i]['key'])
    i = i + 1

############################################################

# PRINTING OUT ALL THE ODDS OF THE GAMES

i = 0
while i < len(all_sports_key):
    url = f"https://odds.p.rapidapi.com/v4/sports/{all_sports_key[i]}/odds"
    querystring = {"regions":"us","oddsFormat":"decimal","markets":"h2h,spreads","dateFormat":"iso"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    writeFile = open(f'json_files/{all_sports_key[i]}.json', 'a+')
    writeFile.write(response.text)
    writeFile.close()
    i = i + 1