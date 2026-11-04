import json

def load_movies_data() -> dict:
    with open("data/movies.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data