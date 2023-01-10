def arbritrage_calc(match):
    
    home_odd = []
    away_odd = []
    draw_odd = []

    i = 0
    while i < len(match):
        
        # WRITE ARBRITRAGE LOGIC HERE

        home_odd.append(match[i].home_team_odd)
        away_odd.append(match[i].away_team_odd)
        draw_odd.append(match[i].draw_odd)

        i = i + 1
    
    odd_1 = max(home_odd)
    odd_2 = max(away_odd)
    odd_3 = max(draw_odd)

    index_1 = home_odd.index(odd_1)
    index_2 = away_odd.index(odd_2)
    index_3 = draw_odd.index(odd_3)

    if odd_3 != 0:
        arb = ((1/odd_1) + (1/odd_2) + (1/odd_3))*100
    else:
        arb = ((1/odd_1) + (1/odd_2))*100


    if arb < 0:
        print("")
        print("ARBRITRAGE OPPORTUNITY FOUND!")
        print(f'PERCENTAGE GAIN = {100-arb}%')
        print(f'{match[index_1].date} {match[index_1].time}')
        print(f'{match[index_1].sport_key}')
        print("")
        print(f'BOOKIE 1 = {match[index_1].bookie}' )
        print(f'{match[index_1].home_team}')
        print(f'ODD = {match[index_1].home_team_odd}')
        print("")
        print(f'BOOKIE 2 = {match[index_2].bookie}' )
        print(f'{match[index_2].home_team}')
        print(f'ODD = {match[index_2].home_team_odd}')
        print("")

        if odd_3 != 0:
            print(f'BOOKIE 3 = {match[index_3].bookie}' )
            print(f'{match[index_3].home_team}')
            print(f'ODD = {match[index_3].home_team_odd}')
            print("")

        print(f'PERCENTAGE GAIN = {100-arb}%')
        print(f'{match[index_1].date} {match[index_1].time}')
        print("")
        print('******************************************************')
    
    else:
        print(f"Arbritrage not found in {match[index_1].id}")



        