import json

def load_movies_data() -> dict:
    with open("data/movies.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

# def load_stop_words() -> list[str]:
#     def remove_punctuations(word: str) -> str:
#         return keyword_search.remove_useless_substring(word, string.punctuation)
#     f = open("data/stopwords.txt", 'r', encoding='utf-8')
#     words = f.read()
#     words = words.splitlines()
#     words = map(remove_punctuations, words)
#     print(words)
#     return words
