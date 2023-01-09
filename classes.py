# PARENT CLASS
class Game:
    def __init__(self, id, sport_key, date, time, home_team, away_team, bookie, home_team_odd, away_team_odd):
        self.id = id
        self.sport_key = sport_key
        self.date = date
        self.time = time
        self.home_team = home_team
        self.away_team = away_team
        self.bookie = bookie
        self.home_team_odd = home_team_odd
        self.away_team_odd = away_team_odd


# CHILD CLASS 1
# CURRENT WORKFLOW IN THIS CLASS
class H2H(Game):
    def __init__(self, id, sport_key, date, time, home_team, away_team, bookie, home_team_odd, away_team_odd, draw_odd):
        super().__init__(id, sport_key, date, time, home_team, away_team, bookie, home_team_odd, away_team_odd)
        self.draw_odd = draw_odd
        

# CHILD CLASS 1
# FOR V2
class Spread(Game):
    def __init__(self, id, sport_key, date, time, home_team, away_team, bookie, home_team_odd, away_team_odd, home_team_spread, away_team_spread):
        super.__init__(id, sport_key, date, time, home_team, away_team, bookie, home_team_odd, away_team_odd)
        self.home_team_spread = home_team_spread
        self.away_team_spread = away_team_spread


