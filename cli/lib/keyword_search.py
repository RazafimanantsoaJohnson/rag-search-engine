import string
# from search_utils import *

# stop_words = load_stop_words()

def keyword_search(movies: list, search_query: str) -> str:
    result = ""
    i = 0
    result_count = 0
    while(i < len(movies) and result_count <5):
        movie = movies[i]
        if check_query(search_query.lower(), movie["title"]):
            result_count +=1
            if result =="":
                result = f"{i}. {movie["title"]}"
            else:
                result = f"{result}\n{i}. {movie["title"]}"
        i += 1
    return result

def check_query(search_query: str, movie_title: str) -> bool:
    query = remove_useless_substring(search_query, string.punctuation)
    title = remove_useless_substring(movie_title, string.punctuation)
    query_tokens = tokenize_query(query)
    title_tokens = tokenize_query(movie_title)
    # for t in query_tokens:
    #     if (t in stop_words):
    #         del t
    # for t in title_tokens:
    #     if (t in stop_words):
    #         del t
    for t in query_tokens:
        if (t in title_tokens):
            return True
    return False

def remove_useless_substring(text: str, substring: str) -> string:
    table = str.maketrans("","", substring)
    result = text.lower()
    return str.translate(result, table)

def tokenize_query(search_query: str) -> list[str]:
    tokens = search_query.split()
    return tokens
