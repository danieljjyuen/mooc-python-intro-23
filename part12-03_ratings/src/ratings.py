# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def rating (item:dict):
        return item["rating"]
    return sorted(items, key=rating, reverse=True)