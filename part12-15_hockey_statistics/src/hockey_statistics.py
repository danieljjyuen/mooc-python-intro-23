# Write your solution here
import json

def print_line(data):
    print(f"{data["name"]:21}{data["team"]:3}{data["goals"]:4} + {data["assists"]:2} = {data["goals"]+data["assists"]:3}")

class Application:

    def __init__(self):
        self.__data = None

    def read_all(self):
        filename = input("file name: ")
        with open(filename) as file_main:
            data = json.load(file_main)
            self.__data = data
        print(f"read the data of {len(data)} players\n")

    def helper(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals\n")
    
    def search_player(self):
        name = input("name: ")
        player = None
        for play in self.__data:
            if play["name"] == name:
                player = play
                break
        print_line(player)

    def list_teams(self):
        teams = sorted(list(set((list(map(lambda x: x["team"], self.__data))))))
        for team in teams:
            print(team)

    def list_countries(self):
        countries = sorted(list(set((list(map(lambda x: x["nationality"], self.__data))))))
        for country in countries:
            print(country)
    
    def list_players_team(self):
        team = input("team: ")
        filtered = list(filter(lambda x: x["team"] == team, self.__data))
        sortedteam = sorted(filtered, key=lambda x : x["goals"] + x["assists"], reverse=True)
        for player in sortedteam:
            print_line(player)

    def list_players_country(self):
        country = input("country: ")
        filtered = list(filter(lambda x: x["nationality"] == country, self.__data))
        sortedteam = sorted(filtered, key=lambda x : x["goals"] + x["assists"], reverse=True)
        for player in sortedteam:
            print_line(player)
                        
    def most_points(self):
        how_many = int(input("how many:"))
        sortedteam = sorted(self.__data, key=lambda x: x["goals"] + x["assists"], reverse=True)
        for i in range(how_many):
            print_line(sortedteam[i])
    
    def most_goals(self):
        how_many = int(input("how many:"))

        sortedteam = sorted(self.__data, key=lambda x: (-x["goals"],x["games"]))
        for i in range(how_many):
            print_line(sortedteam[i])

    def execute(self):
        self.read_all()
        self.helper()
        while True:
            command = input("command: ")

            if command == "1":
                self.search_player()
            elif command == "2":
                self.list_teams()

            elif command == "3":
                self.list_countries()

            elif command == "4":
                self.list_players_team()

            elif command == "5":
                self.list_players_country()

            elif command == "6":
                self.most_points()

            elif command == "7":
                self.most_goals()

            elif command =="0":
                break

    




app = Application()
app.execute()




    #   "name": "Travis Zajac",
    #   "nationality": "CAN",
    #   "assists": 16,
    #   "goals": 9,
    #   "penalties": 28,
    #   "team": "NJD",
    #   "games": 69

    # for lines in json.load(file_main.read()):
    # dict[lines["name"]] = {
    #     "nationality":lines["nationality"],
    #     "assists": int(lines["assists"]),
    #     "goals": int(lines["goals"]),
    #     "penalties": int(lines["penalties"]),
    #     "team": lines["team"],
    #     "games": int(lines["games"])
    # }

