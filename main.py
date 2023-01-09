import json
from datetime import date
from api import make_all_sports, make_all_sports_odd
from classes import Game, H2H


def main():


    ########################################################################
    

    # GETTING ALL SPORTS LIST DATA
    make_all_sports()


    ########################################################################


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


    ########################################################################


    # GETTING ALL SPORTS ODD IN DETAIL WITH THE EXTRACTED KEY NAMES
    make_all_sports_odd(all_sports_key)


    ########################################################################


    # EXTRACT ALL GAMES BY DATE
    # getting date in string
    #today = date.today().strftime('%m-%d-%Y')
    '''
    print(today)
    print(type(today))
    '''

    '''
    # Getting games by TEST
    i = 0
    while i < len(all_sports_key):
        open_odds_file = open(f"json_files/{all_sports_key[i]}.json", 'r')
        data = json.load(open_odds_file)
        
        if len(data) > 0 and isinstance(data, list):
            j = 0
            while j < len(data):
                k = 0
                while k < len(data[j]["bookmakers"]):
                    print(data[j]["bookmakers"][k]["key"])
                    k = k + 1
                j = j + 1
        i = i + 1 
    '''


    ########################################################################
    '''

    # GETTING NUMBER OF GAMES BY DATE
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
    '''

    ########################################################################


    # CREATING A LIST OF GAMES TO HOLD GAME OBJECTS
    game_details = []

    # LOADING ALL DATA INTO H2H CLASS
    i = 0
    while i < len(all_sports_key):
        open_odds_file = open(f"json_files/{all_sports_key[i]}.json", 'r')
        data = json.load(open_odds_file)

        if len(data) > 0 and isinstance(data, list):
            j = 0
            while j < len(data):
                k = 0
                while k < len(data[j]["bookmakers"]):
                    arg_id = data[j]["id"]
                    arg_sport_key = data[j]["sport_key"]
                    arg_date = data[j]["commence_time"][:10]
                    arg_time = data[j]["commence_time"][11:16]
                    arg_home_team = data[j]["home_team"]
                    arg_away_team = data[j]["away_team"]
                    arg_bookie = data[j]["bookmakers"][k]["key"]
                    
                    if data[j]["bookmakers"][k]["markets"][0]["outcomes"][0]["name"] == data[j]["home_team"]:
                        arg_home_team_odd = data[j]["bookmakers"][k]["markets"][0]["outcomes"][0]["price"]
                        arg_away_team_odd = data[j]["bookmakers"][k]["markets"][0]["outcomes"][1]["price"]
                    else:
                        arg_home_team_odd = data[j]["bookmakers"][k]["markets"][0]["outcomes"][1]["price"]
                        arg_away_team_odd = data[j]["bookmakers"][k]["markets"][0]["outcomes"][0]["price"]
                    

                    if len(data[j]["bookmakers"][k]["markets"][0]["outcomes"]) == 3:
                        arg_draw_odd =  data[j]["bookmakers"][k]["markets"][0]["outcomes"][2]["price"]
                    else:
                        arg_draw_odd = 0

                    game_object = H2H(arg_id, arg_sport_key, arg_date, arg_time, arg_home_team, arg_away_team, arg_bookie, arg_home_team_odd, arg_away_team_odd, arg_draw_odd)
                    game_details.append(game_object)

                    k = k + 1

                j = j + 1

        i = i + 1


    ########################################################################


    # PRINTING ALL CLASS OBJECTS - PRINT AS YOU NEED

    for obj in game_details:
        print(obj.id)
        print(obj.draw_odd)
        print("")



    ########################################################################



########################################################################


# ENSURING THAT THE main() FUNCTION IS ONLY CALLED WHEN THE SCRIPT IS RUN DIRECTLY, AND NOT WHEN IT IS IMPORTED BY ANOTHER SCRIPT.
if __name__ == "__main__":
  main()


########################################################################