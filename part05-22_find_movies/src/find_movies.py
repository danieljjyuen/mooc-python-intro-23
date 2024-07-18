# Write your solution here
def find_movies(database: list, search_term: str):
    list = []
    for movies in database:
        if search_term.lower() in movies['name'].lower():
            list.append(movies)
    return list