import requests
import json


########################################################################


# LIST ALL SPORTS
def make_all_sports():

    url = "https://odds.p.rapidapi.com/v4/sports"

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


########################################################################


# PRINTING OUT ALL THE ODDS OF THE GAMES AND SAVING THEM IN json_files
def make_all_sports_odd(all_sports_key):
    url = "https://odds.p.rapidapi.com/v4/sports"

    headers = {
        "X-RapidAPI-Key": "c5c0ac69f8mshea7d5d2e3bcc9e2p1b38bejsn978ca814bd1a",
        "X-RapidAPI-Host": "odds.p.rapidapi.com"
    }  

    i = 0
    while i < len(all_sports_key):
        url = f"https://odds.p.rapidapi.com/v4/sports/{all_sports_key[i]}/odds"
        querystring = {"regions":"us","oddsFormat":"decimal","markets":"h2h,spreads","dateFormat":"iso"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        writeFile = open(f'json_files/{all_sports_key[i]}.json', 'w+')
        writeFile.write(response.text)
        writeFile.close()
        i = i + 1


########################################################################