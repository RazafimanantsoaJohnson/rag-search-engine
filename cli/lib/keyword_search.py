import string

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
    query = preprocess_string(search_query)
    title = preprocess_string(movie_title)
    tokens = tokenize_query(query)
    for t in tokens:
        if t in title:
            return True
    return False

def preprocess_string(text: string) -> string:
    table = str.maketrans("","", string.punctuation)
    result = text.lower()
    return str.translate(result, table)

def tokenize_query(search_query: str) -> list[str]:
    tokens = search_query.split()
    return tokens
