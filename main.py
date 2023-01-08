import json
from datetime import date
from api import make_all_sports, make_all_sports_odd


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


    ########################################################################


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


    ########################################################################





########################################################################


# ENSURING THAT THE main() FUNCTION IS ONLY CALLED WHEN THE SCRIPT IS RUN DIRECTLY, AND NOT WHEN IT IS IMPORTED BY ANOTHER SCRIPT.
if __name__ == "__main__":
  main()


########################################################################