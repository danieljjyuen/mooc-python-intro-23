# Write your solution here:
class Series:
    def __init__(self, title, season, genres):
        self.title = title
        self.season = season
        self.genres = genres
        self.ratecount =0
        self.ratetotal =0
        self.rateavg =0
    def __str__(self):
        rating = ""
        if self.ratecount ==0:
            rating = "no ratings"
        else:
            rating = f"{self.ratecount} ratings, average {self.rateavg :.1f} points"
        return f"{self.title} ({self.season} seasons)\ngenres: {", ".join(self.genres)}\n{rating}"

    def rate(self, rating:int):
        self.ratecount+=1
        self.ratetotal+=rating
        self.rateavg = self.ratetotal/self.ratecount

def minimum_grade(rating:float, series_list:list):
    result = []
    for show in series_list:
        if show.rateavg >= rating:
            result.append(show)
    return result
def includes_genre(genre:str, series_list:list):
    result = []
    for show in series_list:
        if genre in show.genres:
            result.append(show)
    return result
# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# print(dexter)