import string
from nltk import PorterStemmer
from .search_utils import *

stemmer = PorterStemmer()

def keyword_search(movies: list, search_query: str) -> str:
    result = ""
    i = 0
    result_count = 0
    stop_words = process_stop_words()
    while(i < len(movies) and result_count <5):
        movie = movies[i]
        if check_query(search_query.lower(), movie["title"], stop_words):
            result_count +=1
            if result =="":
                result = f"{i}. {movie["title"]}"
            else:
                result = f"{result}\n{i}. {movie["title"]}"
        i += 1
    return result

def check_query(search_query: str, movie_title: str, stop_words: list[str]) -> bool:
    query = remove_useless_substring(search_query, string.punctuation)
    title = remove_useless_substring(movie_title, string.punctuation)
    query_tokens = tokenize_text(query, stop_words)
    title_tokens = tokenize_text(title, stop_words)

    title_str = "".join(title_tokens)
    for t in query_tokens:
        if (t in title_tokens) or (t in title_str):
            return True
    return False

def remove_useless_substring(text: str, substring: str) -> str:
    table = str.maketrans("","", substring)
    result = text.lower()
    return str.translate(result, table)

def tokenize_text(search_query: str, stop_words: list[str]) -> list[str]:
    tokens = search_query.split()
    i = 0
    while (i < len(tokens)):
        t = tokens[i]
        if (t in stop_words):
            tokens.remove(t)
        else:
            tokens[i] = stemmer.stem(t)
        i+= 1
            
    return tokens

def process_stop_words() -> list[str]:
    def remove_punctuation(word: str) -> str:
        return remove_useless_substring(word, string.punctuation)
    stop_words = load_stop_words()
    stop_words = map(remove_punctuation, stop_words)
    return list(stop_words)
    

