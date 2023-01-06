import requests
import json
from datetime import date

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
    writeFile = open(f'json_files/{all_sports_key[i]}.json', 'w+')
    writeFile.write(response.text)
    writeFile.close()
    i = i + 1

############################################################

# EXTRACT ALL GAMES BY DATE
# date
# game name (team 1 vs team 2)
# total number of games

# getting date in string
today = date.today().strftime('%m-%d-%Y')
'''
print(today)
print(type(today))
'''

'''
# Getting games by DATE
i = 0
while i < len(all_sports_key):
    open_odds_file = open(f"json_files/{all_sports_key[i]}.json", 'r')
    data = json.load(open_odds_file)
    
    if len(data) > 0 and isinstance(data, list):
        j = 0
        while j < len(data):
            print(data[j]["commence_time"][:10])
            j = j + 1
    i = i + 1 
'''


# Getting number of games by DATE

total_games_by_date = dict()

i = 0
while i < len(all_sports_key):
    open_odds_file = open(f"json_files/{all_sports_key[i]}.json", 'r')
    data = json.load(open_odds_file)
    
    if len(data) > 0 and isinstance(data, list):
        j = 0
        while j < len(data):
            if (data[j]["commence_time"][:10]) not in total_games_by_date:
                total_games_by_date[(data[j]["commence_time"][:10])] = 1
            else:
                total_games_by_date[(data[j]["commence_time"][:10])] += 1
            j = j + 1
    i = i + 1 

print((total_games_by_date))
